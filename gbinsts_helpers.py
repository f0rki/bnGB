from binaryninja import (Architecture, LowLevelILOperation, LowLevelILLabel,
                         log_info, LLIL_TEMP)


def add_trunc(a, b, bits=16):
    maxval = (1 << bits) - 1
    r = a + b
    return r & maxval


def _get_2b_reg(il, register):
    register = register.lower()
    return il.reg_split(1, register[0], register[1])


def jump(il, addr, imm, iinfo):
    length = iinfo['length']
    dest = None

    if 'operand2' not in iinfo:
        # unconditional jump
        lbl = None
        if imm[0] is not None:
            # log_info(str(iinfo) + str(imm))
            dest = il.const_pointer(2, imm[0])
            if iinfo['mnemonic'] == "JR":
                lbl = il.get_label_for_address(il.arch,
                                               add_trunc(imm[0], addr, 16))
                # dest = il.add(2, dest, il.const_pointer(2, il.current_address))
                x = add_trunc(imm[0], il.current_address + length, 16)
                dest = il.const_pointer(2, x)
            else:
                lbl = il.get_label_for_address(il.arch, imm[0])

            if lbl is None:
                return il.jump(dest)
            else:
                return il.goto(lbl)
        else:
            a2 = iinfo['operand1']
            if a2 == '(HL)':
                return il.jump(_get_2b_reg(il, "HL"))
            else:
                return il.unimplemented()
    else:
        # conditional jump

        # build condition expression
        cond_type = iinfo['operand1']
        cond = il.flag(cond_type[-1].lower())
        if cond_type[0] == "N":
            cond = il.not_expr(1, cond)

        # jump target
        target = None
        if imm[1] is not None:
            if iinfo['mnemonic'] == "JR":
                x = add_trunc(imm[1], il.current_address + length, 16)
                target = il.get_label_for_address(il.arch, x)
                dest = il.const_pointer(2, x)
            else:
                target = il.get_label_for_address(il.arch, imm[1])
                dest = il.const_pointer(2, imm[1])
        else:
            log_info(str(imm))
            raise NotImplementedError()

        t_mark = False
        if target is None:
            target = LowLevelILLabel()
            t_mark = True

        # fallthrough
        fallthrough = il.get_label_for_address(il.arch,
                                               il.current_address + length)
        f_mark = False
        if fallthrough is None:
            fallthrough = LowLevelILLabel()
            f_mark = True

        # if (cond) jump(target) else jump(fallthrough)

        il.append(il.if_expr(cond, target, fallthrough))

        if t_mark:
            il.mark_label(target)
            il.append(il.jump(dest))

        if f_mark:
            il.mark_label(fallthrough)

    return []


# def load(il, addr, imm, iinfo):
#     if 'operand1' in iinfo:
#         op1 = iinfo['operand1']
#         if 'operand2' in iinfo:
#             op2 = iinfo['operand1']
#             # if imm[0] is None and imm[1] is None:
#             #     if len(op1) == 1:
#             #         return il.set_reg(1, op1, il.reg())
#             #     elif len(op1) == 2:
#             pass
#         else:
#             if imm[1] is not None: if len(op1) == 1: return il.set_reg(1, il.const(1, imm[1]))
#                 elif op1 == "SP":
#                     return il.set_reg(2, il.const(2, imm[1]))
#                 elif len(op1) == 2:
#                     return il.set_reg_split(1, op1[0], op1[1], il.const(1, imm[1]))
#     else:
#         raise NotImplementedError()


def push16(il, addr, imm, iinfo):
    hi, lo = iinfo['operand1'].lower()
    regval = il.reg_split(1, hi, lo)
    return il.push(2, regval)


def pop16(il, addr, imm, iinfo):
    hi, lo = iinfo['operand1'].lower()
    tmp = LLIL_TEMP(0)
    il.append(il.set_reg(2, tmp, il.pop(2)))
    il.append(il.set_reg_split(1, hi, lo, il.reg(2, tmp)))
    return []


def load_imm(il, addr, imm, iinfo):
    reg = iinfo['operand1'].lower()
    if len(reg) == 1:
        return il.set_reg(1, reg, il.const(1, imm[1]))
    elif len(reg) == 2:
        return il.set_reg_split(1, reg[0], reg[1], il.const(2, imm[1]))
    else:
        raise NotImplementedError()


def load16_imm16(il, addr, imm, iinfo):
    return il.set_reg(2, iinfo['operand1'].lower(), il.const(2, imm[1]))


def _load_from_mem(il, X, size):
    if isinstance(X, int):
        src = il.const_pointer(2, X & 0xffff)
    elif isinstance(X, str):
        X = X.lower()
        if X == "sp":
            src = il.reg(2, "sp")
        elif len(X) == 2:
            hi, lo = X.lower()
            src = il.reg_split(1, hi, lo)
        elif len(X) == 1:
            src = il.add(2, il.reg(1, X), il.const(2, 0xff00))
        else:
            return None
    else:
        src = X

    return il.load(size, src)


def set_reg8_from_mem(il, addr, imm, iinfo):
    reg = iinfo['operand1'].lower()
    addr = iinfo['operand2'][1:-1].lower()
    return il.set_reg(1, reg, _load_from_mem(il, addr, 1))


def store_reg8_to_mem(il, addr, imm, iinfo):
    addr = iinfo['operand1'][1:-1].lower()
    reg = iinfo['operand2'].lower()
    if len(addr) == 1:
        addr = il.add(2, il.reg(1, reg), il.const_pointer(2, 0xff00))
    return _store_to_mem(il, addr, reg, 1)


def _store_to_mem(il, A, V, size=1):
    if isinstance(A, int):
        addr = il.const_pointer(2, A & 0xffff)
    elif isinstance(A, str):
        A = A.lower()
        if A == "sp":
            addr = il.reg(2, "sp")
        elif len(A) == 2:
            hi, lo = A.lower()
            addr = il.reg_split(1, hi, lo)
        elif len(A) == 1:
            addr = il.add(2, il.reg(1, A), il.const(2, 0xff00))
        else:
            return None
    else:
        addr = A

    if isinstance(V, int):
        val = il.const(size, V)
    elif isinstance(V, str):
        V = V.lower()
        if len(V) == 1:
            val = il.reg(1, V)
        elif V == "sp":
            val = il.reg(2, V)
        elif len(V) == 2:
            hi, lo = V
            val = il.reg_split(1, hi, lo)
        else:
            return None
    else:
        val = V

    return il.store(size, addr, val)


def alu_op(il, addr, imm, iinfo):
    dest = None
    src = None

    def handle_operand(op, immv):
        if immv is not None:
            return il.const(2, immv)
        elif op == "sp":
            return il.reg(2, 'sp')
        elif len(op) == 1:
            return il.reg(1, op1)
        elif len(op) == 2:
            hi, lo = op
            return il.reg_split(1, hi, lo)
        elif op[0] == '(':
            x = _load_from_mem(il, op[1:-1], 1)
            il.append(il.set_reg(2, LLIL_TEMP(0), x))
            return il.reg(2, LLIL_TEMP(0))
        else:
            return None

    result_size = 1
    if 'operand2' in iinfo:
        op1 = iinfo['operand1'].lower()
        dest = handle_operand(op1, imm[0])
        dst_name = op1
        op2 = iinfo['operand2'].lower()
        src = handle_operand(op2, imm[1])
    else:
        dest = il.reg(1, "a")
        dst_name = 'a'
        op1 = iinfo['operand1'].lower()
        src = handle_operand(op1, imm[0])

    dst_name = dst_name.lower()
    if dst_name == "sp" or (len(dst_name) == 2 and imm[1] is not None):
        # 16-bit ALU
        result_size = 2

    op = iinfo['mnemonic'].upper()
    result = None
    flags = []

    if op == "ADD":
        result = il.add(result_size, src, dest, '*')
    elif op == "ADC":
        result = il.add_carry(result_size, src, dest, il.flag('c'), '*')
    elif op == "SUB":
        result = il.sub(result_size, src, dest, '*')
    elif op == "SBC":
        result = il.sub_borrow(result_size, src, dest, il.flag('c'), '*')
    elif op == "AND":
        result = il.or_expr(result_size, src, dest, 'z')
    elif op == "OR":
        result = il.or_expr(result_size, src, dest, 'z')
    elif op == "XOR":
        result = il.xor_expr(result_size, src, dest, 'z')
    elif op == "CP":
        # kind of an oddball here.
        return [
            il.set_flag('z', il.compare_equal(1, dest, src)),
            il.set_flag('n', il.const(1, 1)),
            il.set_flag('h', il.unimplemented()),
            il.set_flag('c', il.compare_unsigned_less_than(1, dest, src))
        ]
    elif op == "INC":
        dest = src
        dst_name = op1
        result = il.add(result_size, src, il.const(1, 1), 'zh')
    elif op == "DEC":
        dest = src
        dst_name = op1
        result = il.sub(result_size, src, il.const(1, 1), 'zh')
    else:
        return None

    for flag, action in zip('znhc', iinfo['flags']):
        if action == "0":
            flags.append(il.set_flag(flag, il.const(1, 0)))
        elif action == "1":
            flags.append(il.set_flag(flag, il.const(1, 1)))
        # elif action == 'Z':
        #     flags.append(
        #         il.set_flag(flag, il.compare_equal(2, result, il.const(2, 0))))
        pass

    if len(dst_name) == 1:
        dst_setter = il.set_reg(1, dst_name, result)
    elif dst_name == "sp":
        dst_setter = il.set_reg(2, "sp", result)
    elif len(dst_name) == 2:
        hi, lo = dst_name
        dst_setter = il.set_reg_split(1, hi, lo, result)
    elif dst_name[0] == '(' and all(x is None for x in imm):
        dst_setter = _store_to_mem(il, dst_name[1:-1], result, result_size)
    else:
        return None
    return ([dst_setter] + flags)

# def mov_reg(dst, src):
#     if len(dst) == 2 and len(src) == 2:
#         return lambda il, addr, imm, iinfo: il.set_reg_split(
#             2, dst[0], dst[1], il.reg_split(1, src[0], src[1]))
#     else:
#         return lambda il, addr, imm, iinfo: il.set_reg(1, dst, il.reg(1, src))


def reg_move(il, addr, imm, iinfo):
    dst = iinfo['operand1'].lower()
    src = iinfo['operand2'].lower()
    return il.set_reg(len(dst), dst, il.reg(len(src), src))
