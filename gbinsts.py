import struct

from binaryninja import log_info

from .gbinsts_unprefixed import unprefixed
from .gbinsts_cbprefixed import cbprefixed


def gb_disassemble_one(data, addr):
    opbyte = data[0]

    def operand_to_imm(iinfo, operand, imm):
        if 'd8' in iinfo[operand] or 'a8' in iinfo[operand]:
            imm += (data[1], )
        elif 'r8' in iinfo[operand]:
            b = data[1]
            if b >= 128:
                b -= 256
            imm += (b, )
        elif 'a16' in iinfo[operand] or 'd16' in iinfo[operand]:
            imm += (struct.unpack("<H", data[1:3])[0], )
        else:
            imm += (None, )
        return imm

    iinfo = None
    imm = tuple()
    if opbyte != 0xcb and unprefixed[opbyte] is not None:
        iinfo = unprefixed[opbyte]
        if 'operand1' in iinfo:
            imm = operand_to_imm(iinfo, 'operand1', imm)
            if 'operand2' in iinfo:
                imm = operand_to_imm(iinfo, 'operand2', imm)
    elif opbyte == 0xcb and opbyte in cbprefixed:
        iinfo = cbprefixed[opbyte]

    return iinfo, imm
