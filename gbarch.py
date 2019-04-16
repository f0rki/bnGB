import struct
import re
import json
import os
from binaryninja import (Architecture, RegisterInfo, FlagRole, InstructionInfo,
                         BranchType, InstructionTextToken,
                         InstructionTextTokenType, BinaryView, SymbolType,
                         Symbol, SymbolType, Endianness, log_warn)

from .gbinsts import gb_disassemble_one


# from https://gis.stackexchange.com/questions/130027/getting-a-plugin-path-using-python-in-qgis
def resolve(name, basepath=None):
    if not basepath:
        basepath = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(basepath, name)


class GB(Architecture):
    name = "GB"
    address_size = 2
    endianess = Endianness.BigEndian
    default_int_size = 1
    max_instr_length = 3
    regs = {
        'a': RegisterInfo('a', 1),
        'b': RegisterInfo('b', 1),
        'c': RegisterInfo('c', 1),
        'd': RegisterInfo('d', 1),
        'e': RegisterInfo('e', 1),
        'f': RegisterInfo('f', 1),
        'h': RegisterInfo('h', 1),
        'l': RegisterInfo('l', 1),
        'sp': RegisterInfo('sp', 2),
        'pc': RegisterInfo('pc', 2),
    }
    stack_pointer = 'sp'
    flags = ["z", "n", "h", "c"]
    flag_write_types = ["*", "czn", "zn", "hc", "zhc", "z", "zh"]
    flag_roles = {
        'z': FlagRole.ZeroFlagRole,
        'n': FlagRole.NegativeSignFlagRole,
        'h': FlagRole.HalfCarryFlagRole,
        'c': FlagRole.CarryFlagRole,
        # interrupts enabled/disabled
        # 'int': FlagRole.SpecialFlagRole,
    }
    flags_written_by_flag_write_type = {
        "*": ["c", "z", "h", "n"],
        "czn": ["c", "z", "n"],
        "zn": ["z", "n"],
        "hc": ['h', 'c'],
        "zhc": ['z', 'h', 'c'],
        "z": ['z'],
        "zh": ['z', 'h']
    }
    # game boy opcodes in json format from https://github.com/lmmendes/game-boy-opcodes
    with open(resolve("opcodes.json"), 'rb') as f:
        opcodes = json.loads(f.read())["unprefixed"]

    def perform_get_instruction_info(self, data, addr):
        opcode = data[0]
        # Get instruction size
        i_info = InstructionInfo()
        try:
            op_info = self.opcodes["0x%x" % opcode]
        except KeyError:
            return None
        i_info.length = op_info['length']
        # Emulate jump instruction
        if op_info is not None:
            if op_info['mnemonic'] == 'JR':
                arg = data[1]
                dest = arg if arg < 128 else (256 - arg) * (-1)
                if opcode == 0x28 or opcode == 0x38:
                    i_info.add_branch(BranchType.TrueBranch, addr + 2 + dest)
                    i_info.add_branch(BranchType.FalseBranch, addr + 2)
                elif opcode == 0x20 or opcode == 0x30:
                    i_info.add_branch(BranchType.TrueBranch, addr + 2)
                    i_info.add_branch(BranchType.FalseBranch, addr + 2 + dest)
                else:
                    i_info.add_branch(BranchType.UnconditionalBranch,
                                      addr + 2 + dest)
            elif op_info['mnemonic'] == 'JP':
                if opcode == 0xe9:
                    i_info.add_branch(BranchType.UnconditionalBranch, 0xdead)
                else:
                    arg = struct.unpack('<H', data[1:3])[0]
                    if opcode == 0xca or opcode == 0xda:
                        i_info.add_branch(BranchType.TrueBranch, arg)
                        i_info.add_branch(BranchType.FalseBranch, addr + 3)
                    elif opcode == 0xc2 or opcode == 0xd2:
                        i_info.add_branch(BranchType.TrueBranch, addr + 3)
                        i_info.add_branch(BranchType.FalseBranch, arg)
                    else:
                        i_info.add_branch(BranchType.UnconditionalBranch, arg)
            elif op_info['mnemonic'] == 'RET':
                i_info.add_branch(BranchType.FunctionReturn)
            elif op_info['mnemonic'] == 'CALL':
                i_info.add_branch(BranchType.CallDestination,
                                  struct.unpack("<H", data[1:3])[0])
        return i_info

    def get_token(self, mnemonic, operand, data):
        if re.search(r'(d|r|a)8', operand) is not None:
            value = data[1]
            if re.match(r'(d|r|a)8', operand) is not None:
                token = InstructionTextToken(
                    InstructionTextTokenType.IntegerToken, "0x%.2x" % value,
                    value)
            elif re.match(r'\(a8\)', operand) is not None:
                token = InstructionTextToken(
                    InstructionTextTokenType.PossibleAddressToken,
                    "0xff%.2x" % value, value | 0xff00)
            else:
                token = InstructionTextToken(
                    InstructionTextTokenType.PossibleAddressToken,
                    "0x%.4x" % value, value)
        elif re.search(r'(d|r|a)16', operand) is not None:
            value = struct.unpack('<H', data[1:3])[0]
            if re.match(r'(d|r|a)16', operand) is not None:
                if mnemonic == "CALL":
                    token = InstructionTextToken(
                        InstructionTextTokenType.DataSymbolToken,
                        "sub_%x" % value, value)
                else:
                    token = InstructionTextToken(
                        InstructionTextTokenType.IntegerToken,
                        "0x%.4x" % value, value)
            else:
                token = InstructionTextToken(
                    InstructionTextTokenType.PossibleAddressToken,
                    "0x%.4x" % value, value)
        elif re.search(r'A|B|C|D|E|F|H|L|(SP)|(PC)', operand) is not None:
            if re.match(r'A|B|C|D|E|F|H|L|(SP)|(PC)', operand) is not None:
                token = InstructionTextToken(
                    InstructionTextTokenType.RegisterToken, operand.lower())
            else:
                token = InstructionTextToken(
                    InstructionTextTokenType.RegisterToken, operand.lower())
        else:
            token = InstructionTextToken(
                InstructionTextTokenType.RegisterToken, operand.lower())
        return token

    def perform_get_instruction_text(self, data, addr):
        tokens = []
        opcode = data[0]
        try:
            op_info = self.opcodes["0x%x" % opcode]
        except KeyError:
            return None
        if op_info is not None:
            tokens.append(
                InstructionTextToken(InstructionTextTokenType.InstructionToken,
                                     op_info['mnemonic'].lower()))
            if 'operand1' in op_info:
                tokens.append(
                    InstructionTextToken(
                        InstructionTextTokenType.OperandSeparatorToken,
                        ''.rjust(8 - len(op_info['mnemonic']))))
                tokens.append(
                    self.get_token(op_info['mnemonic'], op_info['operand1'],
                                   data))
                if 'operand2' in op_info:
                    tokens.append(
                        InstructionTextToken(
                            InstructionTextTokenType.OperandSeparatorToken,
                            ', '))
                    tokens.append(
                        self.get_token(op_info['mnemonic'],
                                       op_info['operand2'], data))
        return tokens, op_info['length']

    def perform_get_instruction_low_level_il(self, data, addr, il):
        inst, imm = gb_disassemble_one(data, addr)
        if not inst:
            return None

        if 'il' in inst:
            try:
                ils = inst['il'](il, addr, imm, inst)
            except Exception as e:
                log_warn("failed to lift:" + str(inst))
                log_warn(str(e))
                raise
            if ils:
                if isinstance(ils, (list, tuple)):
                    for i in ils:
                        il.append(i)
                else:
                    il.append(ils)
            elif ils is None:
                log_warn("unimplemented to lift:" + str(inst))
        else:
            il.append(il.unimplemented())

        return inst['length']
