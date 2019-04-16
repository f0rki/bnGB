from binaryninja import log_warn
from .gbinsts_helpers import (load_imm, load16_imm16, _load_from_mem, jump,
                              reg_move, pop16, push16, alu_op, _store_to_mem,
                              set_reg8_from_mem, store_reg8_to_mem, add_trunc)

unprefixed = [
    {
        'opcode': 0x00,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'NOP',
        'il': lambda il, addr, imm, iinfo: il.nop()
    },
    {
        'opcode': 0x01,
        'cycles': [12],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'LD',
        'operand1': 'BC',
        'operand2': 'd16',
        'il': load_imm
    },
    {
        'opcode': 0x02,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': '(BC)',
        'operand2': 'A',
        'il': (lambda il, addr, imm, iinfo: _store_to_mem(il, "BC", "A", 1))
    },
    {
        'opcode': 0x03,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'INC',
        'operand1': 'BC',
        'il': alu_op
    },
    {
        'opcode': 0x04,
        'cycles': [4],
        'flags': ['Z', '0', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'INC',
        'operand1': 'B',
        'il': alu_op
    },
    {
        'opcode': 0x05,
        'cycles': [4],
        'flags': ['Z', '1', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'DEC',
        'operand1': 'B',
        'il': alu_op
    },
    {
        'opcode': 0x06,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'LD',
        'operand1': 'B',
        'operand2': 'd8',
        'il': load_imm
    },
    {
        'opcode': 0x07,
        'cycles': [4],
        'flags': ['0', '0', '0', 'C'],
        'length': 0x01,
        'mnemonic': 'RLCA'
    },
    {
        'opcode': 0x08,
        'cycles': [20],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'LD',
        'operand1': '(a16)',
        'operand2': 'SP',
        'il': (lambda il, addr, imm, iinfo: _store_to_mem(il, imm[0], "SP", 2))
    },
    {
        'opcode': 0x09,
        'cycles': [8],
        'flags': ['-', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADD',
        'operand1': 'HL',
        'operand2': 'BC',
        'il': alu_op
    },
    {
        'opcode': 0x0a,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'A',
        'operand2': '(BC)',
        'il': set_reg8_from_mem
    },
    {
        'opcode': 0x0b,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'DEC',
        'operand1': 'BC',
        'il': alu_op
    },
    {
        'opcode': 0x0c,
        'cycles': [4],
        'flags': ['Z', '0', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'INC',
        'operand1': 'C',
        'il': alu_op
    },
    {
        'opcode': 0x0d,
        'cycles': [4],
        'flags': ['Z', '1', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'DEC',
        'operand1': 'C',
        'il': alu_op
    },
    {
        'opcode': 0x0e,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'LD',
        'operand1': 'C',
        'operand2': 'd8',
        'il': load_imm
    },
    {
        'opcode': 0x0f,
        'cycles': [4],
        'flags': ['0', '0', '0', 'C'],
        'length': 0x01,
        'mnemonic': 'RRCA'
    },
    {
        'opcode': 0x10,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'STOP',
        'operand1': '0'
    },
    {
        'opcode': 0x11,
        'cycles': [12],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'LD',
        'operand1': 'DE',
        'operand2': 'd16',
        'il': load_imm
    },
    {
        'opcode': 0x12,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': '(DE)',
        'operand2': 'A',
        'il': (lambda il, addr, imm, iinfo: _store_to_mem(il, "de", "a", 1))
    },
    {
        'opcode': 0x13,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'INC',
        'operand1': 'DE',
        'il': alu_op
    },
    {
        'opcode': 0x14,
        'cycles': [4],
        'flags': ['Z', '0', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'INC',
        'operand1': 'D',
        'il': alu_op
    },
    {
        'opcode': 0x15,
        'cycles': [4],
        'flags': ['Z', '1', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'DEC',
        'operand1': 'D',
        'il': alu_op
    },
    {
        'opcode': 0x16,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'LD',
        'operand1': 'D',
        'operand2': 'd8',
        'il': load_imm
    },
    {
        'opcode': 0x17,
        'cycles': [4],
        'flags': ['0', '0', '0', 'C'],
        'length': 0x01,
        'mnemonic': 'RLA'
    },
    {
        'opcode': 0x18,
        'cycles': [12],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'JR',
        'operand1': 'r8',
        'il': jump
    },
    {
        'opcode': 0x19,
        'cycles': [8],
        'flags': ['-', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADD',
        'operand1': 'HL',
        'operand2': 'DE',
        'il': alu_op
    },
    {
        'opcode': 0x1a,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'A',
        'operand2': '(DE)',
        'il': set_reg8_from_mem
    },
    {
        'opcode': 0x1b,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'DEC',
        'operand1': 'DE',
        'il': alu_op
    },
    {
        'opcode': 0x1c,
        'cycles': [4],
        'flags': ['Z', '0', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'INC',
        'operand1': 'E',
        'il': alu_op
    },
    {
        'opcode': 0x1d,
        'cycles': [4],
        'flags': ['Z', '1', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'DEC',
        'operand1': 'E',
        'il': alu_op
    },
    {
        'opcode': 0x1e,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'LD',
        'operand1': 'E',
        'operand2': 'd8',
        'il': load_imm
    },
    {
        'opcode': 0x1f,
        'cycles': [4],
        'flags': ['0', '0', '0', 'C'],
        'length': 0x01,
        'mnemonic': 'RRA'
    },
    {
        'opcode': 0x20,
        'cycles': [12, 0x08],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'JR',
        'operand1': 'NZ',
        'operand2': 'r8',
        'il': jump
    },
    {
        'opcode': 0x21,
        'cycles': [12],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'LD',
        'operand1': 'HL',
        'operand2': 'd16',
        'il': load_imm
    },
    {
        'opcode':
        0x22,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length':
        0x01,
        'mnemonic':
        'LD',
        'operand1':
        '(HL+)',
        'operand2':
        'A',
        'il': (lambda il, addr, imm, iinfo: [
            _store_to_mem(il, "hl", "a", 1),
            il.set_reg_split(
                1, 'h', 'l',
                il.add(2, il.reg_split(1, 'h', 'l'), il.const(1, 1)))
        ])
    },
    {
        'opcode': 0x23,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'INC',
        'operand1': 'HL',
        'il': alu_op
    },
    {
        'opcode': 0x24,
        'cycles': [4],
        'flags': ['Z', '0', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'INC',
        'operand1': 'H',
        'il': alu_op
    },
    {
        'opcode': 0x25,
        'cycles': [4],
        'flags': ['Z', '1', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'DEC',
        'operand1': 'H',
        'il': alu_op
    },
    {
        'opcode': 0x26,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'LD',
        'operand1': 'H',
        'operand2': 'd8',
        'il': load_imm
    },
    {
        'opcode': 0x27,
        'cycles': [4],
        'flags': ['Z', '-', '0', 'C'],
        'length': 0x01,
        'mnemonic': 'DAA'
    },
    {
        'opcode': 0x28,
        'cycles': [12, 0x08],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'JR',
        'operand1': 'Z',
        'operand2': 'r8',
        'il': jump
    },
    {
        'opcode': 0x29,
        'cycles': [8],
        'flags': ['-', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADD',
        'operand1': 'HL',
        'operand2': 'HL',
        'il': alu_op
    },
    {
        'opcode':
        0x2a,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length':
        0x01,
        'mnemonic':
        'LD',
        'operand1':
        'A',
        'operand2':
        '(HL+)',
        'il': (lambda il, addr, imm, iinfo: [
            il.set_reg(1, 'a', _load_from_mem(il, "hl", 1)),
            il.set_reg_split(
                1, 'h', 'l',
                il.add(2, il.reg_split(1, 'h', 'l'), il.const(1, 1)))
        ])
    },
    {
        'opcode': 0x2b,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'DEC',
        'operand1': 'HL',
        'il': alu_op
    },
    {
        'opcode': 0x2c,
        'cycles': [4],
        'flags': ['Z', '0', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'INC',
        'operand1': 'L',
        'il': alu_op
    },
    {
        'opcode': 0x2d,
        'cycles': [4],
        'flags': ['Z', '1', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'DEC',
        'operand1': 'L',
        'il': alu_op
    },
    {
        'opcode': 0x2e,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'LD',
        'operand1': 'L',
        'operand2': 'd8',
        'il': load_imm
    },
    {
        'opcode': 0x2f,
        'cycles': [4],
        'flags': ['-', '1', '1', '-'],
        'length': 0x01,
        'mnemonic': 'CPL'
    },
    {
        'opcode': 0x30,
        'cycles': [12, 0x08],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'JR',
        'operand1': 'NC',
        'operand2': 'r8',
        'il': jump
    },
    {
        'opcode': 0x31,
        'cycles': [12],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'LD',
        'operand1': 'SP',
        'operand2': 'd16',
        'il': load16_imm16
    },
    {
        'opcode':
        0x32,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length':
        0x01,
        'mnemonic':
        'LD',
        'operand1':
        '(HL-)',
        'operand2':
        'A',
        'il': (lambda il, addr, imm, iinfo: [
            _store_to_mem(il, "hl", "a", 1),
            il.set_reg_split(
                1, 'h', 'l',
                il.sub(2, il.reg_split(1, 'h', 'l'), il.const(1, 1)))
        ])
    },
    {
        'opcode': 0x33,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'INC',
        'operand1': 'SP',
        'il': alu_op
    },
    {
        'opcode': 0x34,
        'cycles': [12],
        'flags': ['Z', '0', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'INC',
        'operand1': '(HL)',
        'il': alu_op
    },
    {
        'opcode': 0x35,
        'cycles': [12],
        'flags': ['Z', '1', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'DEC',
        'operand1': '(HL)',
        'il': alu_op
    },
    {
        'opcode': 0x36,
        'cycles': [12],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'LD',
        'operand1': '(HL)',
        'operand2': 'd8',
        'il': (lambda il, addr, imm, iinfo: _store_to_mem(il, "hl", imm[1], 1))
    },
    {
        'opcode': 0x37,
        'cycles': [4],
        'flags': ['-', '0', '0', '1'],
        'length': 0x01,
        'mnemonic': 'SCF'
    },
    {
        'opcode': 0x38,
        'cycles': [12, 0x08],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'JR',
        'operand1': 'C',
        'operand2': 'r8',
        'il': jump
    },
    {
        'opcode': 0x39,
        'cycles': [8],
        'flags': ['-', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADD',
        'operand1': 'HL',
        'operand2': 'SP',
        'il': alu_op
    },
    {
        'opcode':
        0x3a,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length':
        0x01,
        'mnemonic':
        'LD',
        'operand1':
        'A',
        'operand2':
        '(HL-)',
        'il': (lambda il, addr, imm, iinfo: [
            il.set_reg(1, 'a', _load_from_mem(il, "hl", 1)),
            il.set_reg_split(
                1, 'h', 'l',
                il.sub(2, il.reg_split(1, 'h', 'l'), il.const(1, 1)))
        ])
    },
    {
        'opcode': 0x3b,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'DEC',
        'operand1': 'SP',
        'il': alu_op
    },
    {
        'opcode': 0x3c,
        'cycles': [4],
        'flags': ['Z', '0', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'INC',
        'operand1': 'A',
        'il': alu_op
    },
    {
        'opcode': 0x3d,
        'cycles': [4],
        'flags': ['Z', '1', 'H', '-'],
        'length': 0x01,
        'mnemonic': 'DEC',
        'operand1': 'A',
        'il': alu_op
    },
    {
        'opcode': 0x3e,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'LD',
        'operand1': 'A',
        'operand2': 'd8',
        'il': load_imm
    },
    {
        'opcode': 0x3f,
        'cycles': [4],
        'flags': ['-', '0', '0', 'C'],
        'length': 0x01,
        'mnemonic': 'CCF'
    },
    {
        'opcode': 0x40,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'B',
        'operand2': 'B',
        'il': reg_move
    },
    {
        'opcode': 0x41,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'B',
        'operand2': 'C',
        'il': reg_move
    },
    {
        'opcode': 0x42,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'B',
        'operand2': 'D',
        'il': reg_move
    },
    {
        'opcode': 0x43,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'B',
        'operand2': 'E',
        'il': reg_move
    },
    {
        'opcode': 0x44,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'B',
        'operand2': 'H',
        'il': reg_move
    },
    {
        'opcode': 0x45,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'B',
        'operand2': 'L',
        'il': reg_move
    },
    {
        'opcode': 0x46,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'B',
        'operand2': '(HL)',
        'il': set_reg8_from_mem
    },
    {
        'opcode': 0x47,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'B',
        'operand2': 'A',
        'il': reg_move
    },
    {
        'opcode': 0x48,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'C',
        'operand2': 'B',
        'il': reg_move
    },
    {
        'opcode': 0x49,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'C',
        'operand2': 'C',
        'il': reg_move
    },
    {
        'opcode': 0x4a,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'C',
        'operand2': 'D',
        'il': reg_move
    },
    {
        'opcode': 0x4b,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'C',
        'operand2': 'E',
        'il': reg_move
    },
    {
        'opcode': 0x4c,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'C',
        'operand2': 'H',
        'il': reg_move
    },
    {
        'opcode': 0x4d,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'C',
        'operand2': 'L',
        'il': reg_move
    },
    {
        'opcode': 0x4e,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'C',
        'operand2': '(HL)',
        'il': set_reg8_from_mem
    },
    {
        'opcode': 0x4f,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'C',
        'operand2': 'A',
        'il': reg_move
    },
    {
        'opcode': 0x50,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'D',
        'operand2': 'B',
        'il': reg_move
    },
    {
        'opcode': 0x51,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'D',
        'operand2': 'C',
        'il': reg_move
    },
    {
        'opcode': 0x52,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'D',
        'operand2': 'D',
        'il': reg_move
    },
    {
        'opcode': 0x53,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'D',
        'operand2': 'E',
        'il': reg_move
    },
    {
        'opcode': 0x54,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'D',
        'operand2': 'H',
        'il': reg_move
    },
    {
        'opcode': 0x55,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'D',
        'operand2': 'L',
        'il': reg_move
    },
    {
        'opcode': 0x56,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'D',
        'operand2': '(HL)',
        'il': set_reg8_from_mem
    },
    {
        'opcode': 0x57,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'D',
        'operand2': 'A',
        'il': reg_move
    },
    {
        'opcode': 0x58,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'E',
        'operand2': 'B',
        'il': reg_move
    },
    {
        'opcode': 0x59,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'E',
        'operand2': 'C',
        'il': reg_move
    },
    {
        'opcode': 0x5a,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'E',
        'operand2': 'D',
        'il': reg_move
    },
    {
        'opcode': 0x5b,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'E',
        'operand2': 'E',
        'il': reg_move
    },
    {
        'opcode': 0x5c,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'E',
        'operand2': 'H',
        'il': reg_move
    },
    {
        'opcode': 0x5d,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'E',
        'operand2': 'L',
        'il': reg_move
    },
    {
        'opcode': 0x5e,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'E',
        'operand2': '(HL)',
        'il': set_reg8_from_mem
    },
    {
        'opcode': 0x5f,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'E',
        'operand2': 'A',
        'il': reg_move
    },
    {
        'opcode': 0x60,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'H',
        'operand2': 'B',
        'il': reg_move
    },
    {
        'opcode': 0x61,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'H',
        'operand2': 'C',
        'il': reg_move
    },
    {
        'opcode': 0x62,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'H',
        'operand2': 'D',
        'il': reg_move
    },
    {
        'opcode': 0x63,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'H',
        'operand2': 'E',
        'il': reg_move
    },
    {
        'opcode': 0x64,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'H',
        'operand2': 'H',
        'il': reg_move
    },
    {
        'opcode': 0x65,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'H',
        'operand2': 'L',
        'il': reg_move
    },
    {
        'opcode': 0x66,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'H',
        'operand2': '(HL)',
        'il': set_reg8_from_mem
    },
    {
        'opcode': 0x67,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'H',
        'operand2': 'A',
        'il': reg_move
    },
    {
        'opcode': 0x68,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'L',
        'operand2': 'B',
        'il': reg_move
    },
    {
        'opcode': 0x69,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'L',
        'operand2': 'C',
        'il': reg_move
    },
    {
        'opcode': 0x6a,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'L',
        'operand2': 'D',
        'il': reg_move
    },
    {
        'opcode': 0x6b,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'L',
        'operand2': 'E',
        'il': reg_move
    },
    {
        'opcode': 0x6c,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'L',
        'operand2': 'H',
        'il': reg_move
    },
    {
        'opcode': 0x6d,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'L',
        'operand2': 'L',
        'il': reg_move
    },
    {
        'opcode': 0x6e,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'L',
        'operand2': '(HL)',
        'il': set_reg8_from_mem
    },
    {
        'opcode': 0x6f,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'L',
        'operand2': 'A',
        'il': reg_move
    },
    {
        'opcode': 0x70,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': '(HL)',
        'operand2': 'B',
        'il': store_reg8_to_mem
    },
    {
        'opcode': 0x71,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': '(HL)',
        'operand2': 'C',
        'il': store_reg8_to_mem
    },
    {
        'opcode': 0x72,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': '(HL)',
        'operand2': 'D',
        'il': store_reg8_to_mem
    },
    {
        'opcode': 0x73,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': '(HL)',
        'operand2': 'E',
        'il': store_reg8_to_mem
    },
    {
        'opcode': 0x74,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': '(HL)',
        'operand2': 'H',
        'il': store_reg8_to_mem
    },
    {
        'opcode': 0x75,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': '(HL)',
        'operand2': 'L',
        'il': store_reg8_to_mem
    },
    {
        'opcode': 0x76,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'HALT'
    },
    {
        'opcode': 0x77,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': '(HL)',
        'operand2': 'A',
        'il': store_reg8_to_mem
    },
    {
        'opcode': 0x78,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'A',
        'operand2': 'B',
        'il': reg_move
    },
    {
        'opcode': 0x79,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'A',
        'operand2': 'C',
        'il': reg_move
    },
    {
        'opcode': 0x7a,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'A',
        'operand2': 'D',
        'il': reg_move
    },
    {
        'opcode': 0x7b,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'A',
        'operand2': 'E',
        'il': reg_move
    },
    {
        'opcode': 0x7c,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'A',
        'operand2': 'H',
        'il': reg_move
    },
    {
        'opcode': 0x7d,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'A',
        'operand2': 'L',
        'il': reg_move
    },
    {
        'opcode': 0x7e,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'A',
        'operand2': '(HL)',
        'il': set_reg8_from_mem
    },
    {
        'opcode': 0x7f,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'A',
        'operand2': 'A',
        'il': reg_move
    },
    {
        'opcode': 0x80,
        'cycles': [4],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADD',
        'operand1': 'A',
        'operand2': 'B',
        'il': alu_op
    },
    {
        'opcode': 0x81,
        'cycles': [4],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADD',
        'operand1': 'A',
        'operand2': 'C',
        'il': alu_op
    },
    {
        'opcode': 0x82,
        'cycles': [4],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADD',
        'operand1': 'A',
        'operand2': 'D',
        'il': alu_op
    },
    {
        'opcode': 0x83,
        'cycles': [4],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADD',
        'operand1': 'A',
        'operand2': 'E',
        'il': alu_op
    },
    {
        'opcode': 0x84,
        'cycles': [4],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADD',
        'operand1': 'A',
        'operand2': 'H',
        'il': alu_op
    },
    {
        'opcode': 0x85,
        'cycles': [4],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADD',
        'operand1': 'A',
        'operand2': 'L',
        'il': alu_op
    },
    {
        'opcode': 0x86,
        'cycles': [8],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADD',
        'operand1': 'A',
        'operand2': '(HL)',
        'il': alu_op
    },
    {
        'opcode': 0x87,
        'cycles': [4],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADD',
        'operand1': 'A',
        'operand2': 'A',
        'il': alu_op
    },
    {
        'opcode': 0x88,
        'cycles': [4],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADC',
        'operand1': 'A',
        'operand2': 'B',
        'il': alu_op
    },
    {
        'opcode': 0x89,
        'cycles': [4],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADC',
        'operand1': 'A',
        'operand2': 'C',
        'il': alu_op
    },
    {
        'opcode': 0x8a,
        'cycles': [4],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADC',
        'operand1': 'A',
        'operand2': 'D',
        'il': alu_op
    },
    {
        'opcode': 0x8b,
        'cycles': [4],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADC',
        'operand1': 'A',
        'operand2': 'E',
        'il': alu_op
    },
    {
        'opcode': 0x8c,
        'cycles': [4],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADC',
        'operand1': 'A',
        'operand2': 'H',
        'il': alu_op
    },
    {
        'opcode': 0x8d,
        'cycles': [4],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADC',
        'operand1': 'A',
        'operand2': 'L',
        'il': alu_op
    },
    {
        'opcode': 0x8e,
        'cycles': [8],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADC',
        'operand1': 'A',
        'operand2': '(HL)',
        'il': alu_op
    },
    {
        'opcode': 0x8f,
        'cycles': [4],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'ADC',
        'operand1': 'A',
        'operand2': 'A',
        'il': alu_op
    },
    {
        'opcode': 0x90,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SUB',
        'operand1': 'B',
        'il': alu_op
    },
    {
        'opcode': 0x91,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SUB',
        'operand1': 'C',
        'il': alu_op
    },
    {
        'opcode': 0x92,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SUB',
        'operand1': 'D',
        'il': alu_op
    },
    {
        'opcode': 0x93,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SUB',
        'operand1': 'E',
        'il': alu_op
    },
    {
        'opcode': 0x94,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SUB',
        'operand1': 'H',
        'il': alu_op
    },
    {
        'opcode': 0x95,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SUB',
        'operand1': 'L',
        'il': alu_op
    },
    {
        'opcode': 0x96,
        'cycles': [8],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SUB',
        'operand1': '(HL)',
        'il': alu_op
    },
    {
        'opcode': 0x97,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SUB',
        'operand1': 'A',
        'il': alu_op
    },
    {
        'opcode': 0x98,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SBC',
        'operand1': 'A',
        'operand2': 'B',
        'il': alu_op
    },
    {
        'opcode': 0x99,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SBC',
        'operand1': 'A',
        'operand2': 'C',
        'il': alu_op
    },
    {
        'opcode': 0x9a,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SBC',
        'operand1': 'A',
        'operand2': 'D',
        'il': alu_op
    },
    {
        'opcode': 0x9b,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SBC',
        'operand1': 'A',
        'operand2': 'E',
        'il': alu_op
    },
    {
        'opcode': 0x9c,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SBC',
        'operand1': 'A',
        'operand2': 'H',
        'il': alu_op
    },
    {
        'opcode': 0x9d,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SBC',
        'operand1': 'A',
        'operand2': 'L',
        'il': alu_op
    },
    {
        'opcode': 0x9e,
        'cycles': [8],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SBC',
        'operand1': 'A',
        'operand2': '(HL)',
        'il': alu_op
    },
    {
        'opcode': 0x9f,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'SBC',
        'operand1': 'A',
        'operand2': 'A',
        'il': alu_op
    },
    {
        'opcode': 0xa0,
        'cycles': [4],
        'flags': ['Z', '0', '1', '0'],
        'length': 0x01,
        'mnemonic': 'AND',
        'operand1': 'B',
        'il': alu_op
    },
    {
        'opcode': 0xa1,
        'cycles': [4],
        'flags': ['Z', '0', '1', '0'],
        'length': 0x01,
        'mnemonic': 'AND',
        'operand1': 'C',
        'il': alu_op
    },
    {
        'opcode': 0xa2,
        'cycles': [4],
        'flags': ['Z', '0', '1', '0'],
        'length': 0x01,
        'mnemonic': 'AND',
        'operand1': 'D',
        'il': alu_op
    },
    {
        'opcode': 0xa3,
        'cycles': [4],
        'flags': ['Z', '0', '1', '0'],
        'length': 0x01,
        'mnemonic': 'AND',
        'operand1': 'E',
        'il': alu_op
    },
    {
        'opcode': 0xa4,
        'cycles': [4],
        'flags': ['Z', '0', '1', '0'],
        'length': 0x01,
        'mnemonic': 'AND',
        'operand1': 'H',
        'il': alu_op
    },
    {
        'opcode': 0xa5,
        'cycles': [4],
        'flags': ['Z', '0', '1', '0'],
        'length': 0x01,
        'mnemonic': 'AND',
        'operand1': 'L',
        'il': alu_op
    },
    {
        'opcode': 0xa6,
        'cycles': [8],
        'flags': ['Z', '0', '1', '0'],
        'length': 0x01,
        'mnemonic': 'AND',
        'operand1': '(HL)',
        'il': alu_op
    },
    {
        'opcode': 0xa7,
        'cycles': [4],
        'flags': ['Z', '0', '1', '0'],
        'length': 0x01,
        'mnemonic': 'AND',
        'operand1': 'A',
        'il': alu_op
    },
    {
        'opcode': 0xa8,
        'cycles': [4],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'XOR',
        'operand1': 'B',
        'il': alu_op
    },
    {
        'opcode': 0xa9,
        'cycles': [4],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'XOR',
        'operand1': 'C',
        'il': alu_op
    },
    {
        'opcode': 0xaa,
        'cycles': [4],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'XOR',
        'operand1': 'D',
        'il': alu_op
    },
    {
        'opcode': 0xab,
        'cycles': [4],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'XOR',
        'operand1': 'E',
        'il': alu_op
    },
    {
        'opcode': 0xac,
        'cycles': [4],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'XOR',
        'operand1': 'H',
        'il': alu_op
    },
    {
        'opcode': 0xad,
        'cycles': [4],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'XOR',
        'operand1': 'L',
        'il': alu_op
    },
    {
        'opcode': 0xae,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'XOR',
        'operand1': '(HL)',
        'il': alu_op
    },
    {
        'opcode': 0xaf,
        'cycles': [4],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'XOR',
        'operand1': 'A',
        'il': alu_op
    },
    {
        'opcode': 0xb0,
        'cycles': [4],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'OR',
        'operand1': 'B',
        'il': alu_op
    },
    {
        'opcode': 0xb1,
        'cycles': [4],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'OR',
        'operand1': 'C',
        'il': alu_op
    },
    {
        'opcode': 0xb2,
        'cycles': [4],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'OR',
        'operand1': 'D',
        'il': alu_op
    },
    {
        'opcode': 0xb3,
        'cycles': [4],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'OR',
        'operand1': 'E',
        'il': alu_op
    },
    {
        'opcode': 0xb4,
        'cycles': [4],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'OR',
        'operand1': 'H',
        'il': alu_op
    },
    {
        'opcode': 0xb5,
        'cycles': [4],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'OR',
        'operand1': 'L',
        'il': alu_op
    },
    {
        'opcode': 0xb6,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'OR',
        'operand1': '(HL)',
        'il': alu_op
    },
    {
        'opcode': 0xb7,
        'cycles': [4],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x01,
        'mnemonic': 'OR',
        'operand1': 'A',
        'il': alu_op
    },
    {
        'opcode': 0xb8,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'CP',
        'operand1': 'B',
        'il': alu_op
    },
    {
        'opcode': 0xb9,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'CP',
        'operand1': 'C',
        'il': alu_op
    },
    {
        'opcode': 0xba,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'CP',
        'operand1': 'D',
        'il': alu_op
    },
    {
        'opcode': 0xbb,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'CP',
        'operand1': 'E',
        'il': alu_op
    },
    {
        'opcode': 0xbc,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'CP',
        'operand1': 'H',
        'il': alu_op
    },
    {
        'opcode': 0xbd,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'CP',
        'operand1': 'L',
        'il': alu_op
    },
    {
        'opcode': 0xbe,
        'cycles': [8],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'CP',
        'operand1': '(HL)',
        'il': alu_op
    },
    {
        'opcode': 0xbf,
        'cycles': [4],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'CP',
        'operand1': 'A',
        'il': alu_op
    },
    {
        'opcode': 0xc0,
        'cycles': [20, 0x08],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'RET',
        'operand1': 'NZ'
    },
    {
        'opcode': 0xc1,
        'cycles': [12],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'POP',
        'operand1': 'BC',
        'il': pop16
    },
    {
        'opcode': 0xc2,
        'cycles': [16, 0x0c],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'JP',
        'operand1': 'NZ',
        'operand2': 'a16',
        'il': jump
    },
    {
        'opcode': 0xc3,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'JP',
        'operand1': 'a16',
        'il': jump
    },
    {
        'opcode': 0xc4,
        'cycles': [24, 0x0c],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'CALL',
        'operand1': 'NZ',
        'operand2': 'a16'
    },
    {
        'opcode': 0xc5,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'PUSH',
        'operand1': 'BC',
        'il': push16
    },
    {
        'opcode': 0xc6,
        'cycles': [8],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x02,
        'mnemonic': 'ADD',
        'operand1': 'A',
        'operand2': 'd8',
        'il': alu_op
    },
    {
        'opcode': 0xc7,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'RST',
        'operand1': '00H'
    },
    {
        'opcode': 0xc8,
        'cycles': [20, 0x08],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'RET',
        'operand1': 'Z'
    },
    {
        'opcode': 0xc9,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'RET'
    },
    {
        'opcode': 0xca,
        'cycles': [16, 0x0c],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'JP',
        'operand1': 'Z',
        'operand2': 'a16',
        'il': jump
    },
    {
        'opcode': 0xcb,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'PREFIX',
        'operand1': 'CB'
    },
    {
        'opcode': 0xcc,
        'cycles': [24, 0x0c],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'CALL',
        'operand1': 'Z',
        'operand2': 'a16'
    },
    {
        'opcode': 0xcd,
        'cycles': [24],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'CALL',
        'operand1': 'a16'
    },
    {
        'opcode': 0xce,
        'cycles': [8],
        'flags': ['Z', '0', 'H', 'C'],
        'length': 0x02,
        'mnemonic': 'ADC',
        'operand1': 'A',
        'operand2': 'd8',
        'il': alu_op
    },
    {
        'opcode': 0xcf,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'RST',
        'operand1': '08H'
    },
    {
        'opcode': 0xd0,
        'cycles': [20, 0x08],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'RET',
        'operand1': 'NC'
    },
    {
        'opcode': 0xd1,
        'cycles': [12],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'POP',
        'operand1': 'DE',
        'il': pop16
    },
    {
        'opcode': 0xd2,
        'cycles': [16, 0x0c],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'JP',
        'operand1': 'NC',
        'operand2': 'a16',
        'il': jump
    },
    None,
    {
        'opcode': 0xd4,
        'cycles': [24, 0x0c],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'CALL',
        'operand1': 'NC',
        'operand2': 'a16'
    },
    {
        'opcode': 0xd5,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'PUSH',
        'operand1': 'DE',
        'il': push16
    },
    {
        'opcode': 0xd6,
        'cycles': [8],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x02,
        'mnemonic': 'SUB',
        'operand1': 'd8',
        'il': alu_op
    },
    {
        'opcode': 0xd7,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'RST',
        'operand1': '10H'
    },
    {
        'opcode': 0xd8,
        'cycles': [20, 0x08],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'RET',
        'operand1': 'C'
    },
    {
        'opcode': 0xd9,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'RETI'
    },
    {
        'opcode': 0xda,
        'cycles': [16, 0x0c],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'JP',
        'operand1': 'C',
        'operand2': 'a16',
        'il': jump
    },
    None,
    {
        'opcode': 0xdc,
        'cycles': [24, 0x0c],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'CALL',
        'operand1': 'C',
        'operand2': 'a16'
    },
    None,
    {
        'opcode': 0xde,
        'cycles': [8],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x02,
        'mnemonic': 'SBC',
        'operand1': 'A',
        'operand2': 'd8',
        'il': alu_op
    },
    {
        'opcode': 0xdf,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'RST',
        'operand1': '18H'
    },
    {
        'opcode':
        0xe0,
        'cycles': [12],
        'flags': ['-', '-', '-', '-'],
        'length':
        0x02,
        'mnemonic':
        'LDH',
        'operand1':
        '(a8)',
        'operand2':
        'A',
        'il': (lambda il, addr, imm, iinfo: _store_to_mem(
            il, 0xff00 + imm[0], 'a', 1))
    },
    {
        'opcode': 0xe1,
        'cycles': [12],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'POP',
        'operand1': 'HL',
        'il': pop16
    },
    {
        'opcode': 0xe2,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'LD',
        'operand1': '(C)',
        'operand2': 'A',
        'il': store_reg8_to_mem
    },
    None,
    None,
    {
        'opcode': 0xe5,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'PUSH',
        'operand1': 'HL',
        'il': push16
    },
    {
        'opcode': 0xe6,
        'cycles': [8],
        'flags': ['Z', '0', '1', '0'],
        'length': 0x02,
        'mnemonic': 'AND',
        'operand1': 'd8',
        'il': alu_op
    },
    {
        'opcode': 0xe7,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'RST',
        'operand1': '20H'
    },
    {
        'opcode': 0xe8,
        'cycles': [16],
        'flags': ['0', '0', 'H', 'C'],
        'length': 0x02,
        'mnemonic': 'ADD',
        'operand1': 'SP',
        'operand2': 'r8',
        'il': alu_op
    },
    {
        'opcode': 0xe9,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'JP',
        'operand1': '(HL)',
        'il': jump
    },
    {
        'opcode': 0xea,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x03,
        'mnemonic': 'LD',
        'operand1': '(a16)',
        'operand2': 'A',
        'il': (lambda il, addr, imm, iinfo: _store_to_mem(il, imm[0], 'a', 1))
    },
    None,
    None,
    None,
    {
        'opcode': 0xee,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'XOR',
        'operand1': 'd8',
        'il': alu_op
    },
    {
        'opcode': 0xef,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'RST',
        'operand1': '28H'
    },
    {
        'opcode':
        0xf0,
        'cycles': [12],
        'flags': ['-', '-', '-', '-'],
        'length':
        0x02,
        'mnemonic':
        'LDH',
        'operand1':
        'A',
        'operand2':
        '(a8)',
        'il': (lambda il, addr, imm, iinfo: il.set_reg(
            1, 'a', _load_from_mem(il, 0xff00 + imm[1], 1)))
    },
    {
        'opcode': 0xf1,
        'cycles': [12],
        'flags': ['Z', 'N', 'H', 'C'],
        'length': 0x01,
        'mnemonic': 'POP',
        'operand1': 'AF',
        'il': pop16
    },
    {
        'opcode': 0xf2,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'LD',
        'operand1': 'A',
        'operand2': '(C)',
        'il': set_reg8_from_mem
    },
    {
        'opcode': 0xf3,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'DI',
        # 'il': (lambda il, addr, imm, iinfo: il.set_flag('int', il.const(1, 1)))
        'il': (lambda il, addr, imm, iinfo: il.nop())
    },
    None,
    {
        'opcode': 0xf5,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'PUSH',
        'operand1': 'AF',
        'il': push16
    },
    {
        'opcode': 0xf6,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'OR',
        'operand1': 'd8',
        'il': alu_op
    },
    {
        'opcode': 0xf7,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'RST',
        'operand1': '30H'
    },
    {
        'opcode':
        0xf8,
        'cycles': [12],
        'flags': ['0', '0', 'H', 'C'],
        'length':
        0x02,
        'mnemonic':
        'LD',
        'operand1':
        'HL',
        'operand2':
        'SP+r8',
        'il': (lambda il, addr, imm, iinfo: il.set_reg_split(
            1, 'h', 'l',
            il.load(2, il.add(2, il.const(1, imm[1]), il.reg(2, 'sp')))))
    },
    {
        'opcode': 0xf9,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'LD',
        'operand1': 'SP',
        'operand2': 'HL',
        'il': reg_move
    },
    {
        'opcode':
        0xfa,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length':
        0x03,
        'mnemonic':
        'LD',
        'operand1':
        'A',
        'operand2':
        '(a16)',
        'il': (lambda il, addr, imm, iinfo: il.set_reg(
            1, 'a', _load_from_mem(il, imm[1], 1)))
    },
    {
        'opcode': 0xfb,
        'cycles': [4],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'EI',
        # 'il': (lambda il, addr, imm, iinfo: il.set_flag('int', il.const(1, 0)))
        'il': (lambda il, addr, imm, iinfo: il.nop())
    },
    None,
    None,
    {
        'opcode': 0xfe,
        'cycles': [8],
        'flags': ['Z', '1', 'H', 'C'],
        'length': 0x02,
        'mnemonic': 'CP',
        'operand1': 'd8',
        'il': alu_op
    },
    {
        'opcode': 0xff,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x01,
        'mnemonic': 'RST',
        'operand1': '38H'
    }
]

for k, v in enumerate(unprefixed):
    if k != 0xcb and v and 'il' not in v:
        log_warn("missing IL definition for {} 0x{:x}".format(
            v['mnemonic'], k))
