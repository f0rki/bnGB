from .gbinsts_helpers import *  # noqa

cbprefixed = {
    0x00: {
        'addr': 0x00,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RLC',
        'operand1': 'B'
    },
    0x01: {
        'addr': 0x01,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RLC',
        'operand1': 'C'
    },
    0x02: {
        'addr': 0x02,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RLC',
        'operand1': 'D'
    },
    0x03: {
        'addr': 0x03,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RLC',
        'operand1': 'E'
    },
    0x04: {
        'addr': 0x04,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RLC',
        'operand1': 'H'
    },
    0x05: {
        'addr': 0x05,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RLC',
        'operand1': 'L'
    },
    0x06: {
        'addr': 0x06,
        'cycles': [16],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RLC',
        'operand1': '(HL)'
    },
    0x07: {
        'addr': 0x07,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RLC',
        'operand1': 'A'
    },
    0x08: {
        'addr': 0x08,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RRC',
        'operand1': 'B'
    },
    0x09: {
        'addr': 0x09,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RRC',
        'operand1': 'C'
    },
    0x0a: {
        'addr': 0x0a,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RRC',
        'operand1': 'D'
    },
    0x0b: {
        'addr': 0x0b,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RRC',
        'operand1': 'E'
    },
    0x0c: {
        'addr': 0x0c,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RRC',
        'operand1': 'H'
    },
    0x0d: {
        'addr': 0x0d,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RRC',
        'operand1': 'L'
    },
    0x0e: {
        'addr': 0x0e,
        'cycles': [16],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RRC',
        'operand1': '(HL)'
    },
    0x0f: {
        'addr': 0x0f,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RRC',
        'operand1': 'A'
    },
    0x10: {
        'addr': 0x10,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RL',
        'operand1': 'B'
    },
    0x11: {
        'addr': 0x11,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RL',
        'operand1': 'C'
    },
    0x12: {
        'addr': 0x12,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RL',
        'operand1': 'D'
    },
    0x13: {
        'addr': 0x13,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RL',
        'operand1': 'E'
    },
    0x14: {
        'addr': 0x14,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RL',
        'operand1': 'H'
    },
    0x15: {
        'addr': 0x15,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RL',
        'operand1': 'L'
    },
    0x16: {
        'addr': 0x16,
        'cycles': [16],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RL',
        'operand1': '(HL)'
    },
    0x17: {
        'addr': 0x17,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RL',
        'operand1': 'A'
    },
    0x18: {
        'addr': 0x18,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RR',
        'operand1': 'B'
    },
    0x19: {
        'addr': 0x19,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RR',
        'operand1': 'C'
    },
    0x1a: {
        'addr': 0x1a,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RR',
        'operand1': 'D'
    },
    0x1b: {
        'addr': 0x1b,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RR',
        'operand1': 'E'
    },
    0x1c: {
        'addr': 0x1c,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RR',
        'operand1': 'H'
    },
    0x1d: {
        'addr': 0x1d,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RR',
        'operand1': 'L'
    },
    0x1e: {
        'addr': 0x1e,
        'cycles': [16],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RR',
        'operand1': '(HL)'
    },
    0x1f: {
        'addr': 0x1f,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'RR',
        'operand1': 'A'
    },
    0x20: {
        'addr': 0x20,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SLA',
        'operand1': 'B'
    },
    0x21: {
        'addr': 0x21,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SLA',
        'operand1': 'C'
    },
    0x22: {
        'addr': 0x22,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SLA',
        'operand1': 'D'
    },
    0x23: {
        'addr': 0x23,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SLA',
        'operand1': 'E'
    },
    0x24: {
        'addr': 0x24,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SLA',
        'operand1': 'H'
    },
    0x25: {
        'addr': 0x25,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SLA',
        'operand1': 'L'
    },
    0x26: {
        'addr': 0x26,
        'cycles': [16],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SLA',
        'operand1': '(HL)'
    },
    0x27: {
        'addr': 0x27,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SLA',
        'operand1': 'A'
    },
    0x28: {
        'addr': 0x28,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SRA',
        'operand1': 'B'
    },
    0x29: {
        'addr': 0x29,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SRA',
        'operand1': 'C'
    },
    0x2a: {
        'addr': 0x2a,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SRA',
        'operand1': 'D'
    },
    0x2b: {
        'addr': 0x2b,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SRA',
        'operand1': 'E'
    },
    0x2c: {
        'addr': 0x2c,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SRA',
        'operand1': 'H'
    },
    0x2d: {
        'addr': 0x2d,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SRA',
        'operand1': 'L'
    },
    0x2e: {
        'addr': 0x2e,
        'cycles': [16],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SRA',
        'operand1': '(HL)'
    },
    0x2f: {
        'addr': 0x2f,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SRA',
        'operand1': 'A'
    },
    0x30: {
        'addr': 0x30,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SWAP',
        'operand1': 'B'
    },
    0x31: {
        'addr': 0x31,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SWAP',
        'operand1': 'C'
    },
    0x32: {
        'addr': 0x32,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SWAP',
        'operand1': 'D'
    },
    0x33: {
        'addr': 0x33,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SWAP',
        'operand1': 'E'
    },
    0x34: {
        'addr': 0x34,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SWAP',
        'operand1': 'H'
    },
    0x35: {
        'addr': 0x35,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SWAP',
        'operand1': 'L'
    },
    0x36: {
        'addr': 0x36,
        'cycles': [16],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SWAP',
        'operand1': '(HL)'
    },
    0x37: {
        'addr': 0x37,
        'cycles': [8],
        'flags': ['Z', '0', '0', '0'],
        'length': 0x02,
        'mnemonic': 'SWAP',
        'operand1': 'A'
    },
    0x38: {
        'addr': 0x38,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SRL',
        'operand1': 'B'
    },
    0x39: {
        'addr': 0x39,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SRL',
        'operand1': 'C'
    },
    0x3a: {
        'addr': 0x3a,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SRL',
        'operand1': 'D'
    },
    0x3b: {
        'addr': 0x3b,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SRL',
        'operand1': 'E'
    },
    0x3c: {
        'addr': 0x3c,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SRL',
        'operand1': 'H'
    },
    0x3d: {
        'addr': 0x3d,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SRL',
        'operand1': 'L'
    },
    0x3e: {
        'addr': 0x3e,
        'cycles': [16],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SRL',
        'operand1': '(HL)'
    },
    0x3f: {
        'addr': 0x3f,
        'cycles': [8],
        'flags': ['Z', '0', '0', 'C'],
        'length': 0x02,
        'mnemonic': 'SRL',
        'operand1': 'A'
    },
    0x40: {
        'addr': 0x40,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '0',
        'operand2': 'B'
    },
    0x41: {
        'addr': 0x41,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '0',
        'operand2': 'C'
    },
    0x42: {
        'addr': 0x42,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '0',
        'operand2': 'D'
    },
    0x43: {
        'addr': 0x43,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '0',
        'operand2': 'E'
    },
    0x44: {
        'addr': 0x44,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '0',
        'operand2': 'H'
    },
    0x45: {
        'addr': 0x45,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '0',
        'operand2': 'L'
    },
    0x46: {
        'addr': 0x46,
        'cycles': [16],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '0',
        'operand2': '(HL)'
    },
    0x47: {
        'addr': 0x47,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '0',
        'operand2': 'A'
    },
    0x48: {
        'addr': 0x48,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '1',
        'operand2': 'B'
    },
    0x49: {
        'addr': 0x49,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '1',
        'operand2': 'C'
    },
    0x4a: {
        'addr': 0x4a,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '1',
        'operand2': 'D'
    },
    0x4b: {
        'addr': 0x4b,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '1',
        'operand2': 'E'
    },
    0x4c: {
        'addr': 0x4c,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '1',
        'operand2': 'H'
    },
    0x4d: {
        'addr': 0x4d,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '1',
        'operand2': 'L'
    },
    0x4e: {
        'addr': 0x4e,
        'cycles': [16],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '1',
        'operand2': '(HL)'
    },
    0x4f: {
        'addr': 0x4f,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '1',
        'operand2': 'A'
    },
    0x50: {
        'addr': 0x50,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '2',
        'operand2': 'B'
    },
    0x51: {
        'addr': 0x51,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '2',
        'operand2': 'C'
    },
    0x52: {
        'addr': 0x52,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '2',
        'operand2': 'D'
    },
    0x53: {
        'addr': 0x53,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '2',
        'operand2': 'E'
    },
    0x54: {
        'addr': 0x54,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '2',
        'operand2': 'H'
    },
    0x55: {
        'addr': 0x55,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '2',
        'operand2': 'L'
    },
    0x56: {
        'addr': 0x56,
        'cycles': [16],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '2',
        'operand2': '(HL)'
    },
    0x57: {
        'addr': 0x57,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '2',
        'operand2': 'A'
    },
    0x58: {
        'addr': 0x58,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '3',
        'operand2': 'B'
    },
    0x59: {
        'addr': 0x59,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '3',
        'operand2': 'C'
    },
    0x5a: {
        'addr': 0x5a,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '3',
        'operand2': 'D'
    },
    0x5b: {
        'addr': 0x5b,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '3',
        'operand2': 'E'
    },
    0x5c: {
        'addr': 0x5c,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '3',
        'operand2': 'H'
    },
    0x5d: {
        'addr': 0x5d,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '3',
        'operand2': 'L'
    },
    0x5e: {
        'addr': 0x5e,
        'cycles': [16],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '3',
        'operand2': '(HL)'
    },
    0x5f: {
        'addr': 0x5f,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '3',
        'operand2': 'A'
    },
    0x60: {
        'addr': 0x60,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '4',
        'operand2': 'B'
    },
    0x61: {
        'addr': 0x61,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '4',
        'operand2': 'C'
    },
    0x62: {
        'addr': 0x62,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '4',
        'operand2': 'D'
    },
    0x63: {
        'addr': 0x63,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '4',
        'operand2': 'E'
    },
    0x64: {
        'addr': 0x64,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '4',
        'operand2': 'H'
    },
    0x65: {
        'addr': 0x65,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '4',
        'operand2': 'L'
    },
    0x66: {
        'addr': 0x66,
        'cycles': [16],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '4',
        'operand2': '(HL)'
    },
    0x67: {
        'addr': 0x67,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '4',
        'operand2': 'A'
    },
    0x68: {
        'addr': 0x68,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '5',
        'operand2': 'B'
    },
    0x69: {
        'addr': 0x69,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '5',
        'operand2': 'C'
    },
    0x6a: {
        'addr': 0x6a,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '5',
        'operand2': 'D'
    },
    0x6b: {
        'addr': 0x6b,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '5',
        'operand2': 'E'
    },
    0x6c: {
        'addr': 0x6c,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '5',
        'operand2': 'H'
    },
    0x6d: {
        'addr': 0x6d,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '5',
        'operand2': 'L'
    },
    0x6e: {
        'addr': 0x6e,
        'cycles': [16],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '5',
        'operand2': '(HL)'
    },
    0x6f: {
        'addr': 0x6f,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '5',
        'operand2': 'A'
    },
    0x70: {
        'addr': 0x70,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '6',
        'operand2': 'B'
    },
    0x71: {
        'addr': 0x71,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '6',
        'operand2': 'C'
    },
    0x72: {
        'addr': 0x72,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '6',
        'operand2': 'D'
    },
    0x73: {
        'addr': 0x73,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '6',
        'operand2': 'E'
    },
    0x74: {
        'addr': 0x74,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '6',
        'operand2': 'H'
    },
    0x75: {
        'addr': 0x75,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '6',
        'operand2': 'L'
    },
    0x76: {
        'addr': 0x76,
        'cycles': [16],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '6',
        'operand2': '(HL)'
    },
    0x77: {
        'addr': 0x77,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '6',
        'operand2': 'A'
    },
    0x78: {
        'addr': 0x78,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '7',
        'operand2': 'B'
    },
    0x79: {
        'addr': 0x79,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '7',
        'operand2': 'C'
    },
    0x7a: {
        'addr': 0x7a,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '7',
        'operand2': 'D'
    },
    0x7b: {
        'addr': 0x7b,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '7',
        'operand2': 'E'
    },
    0x7c: {
        'addr': 0x7c,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '7',
        'operand2': 'H'
    },
    0x7d: {
        'addr': 0x7d,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '7',
        'operand2': 'L'
    },
    0x7e: {
        'addr': 0x7e,
        'cycles': [16],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '7',
        'operand2': '(HL)'
    },
    0x7f: {
        'addr': 0x7f,
        'cycles': [8],
        'flags': ['Z', '0', '1', '-'],
        'length': 0x02,
        'mnemonic': 'BIT',
        'operand1': '7',
        'operand2': 'A'
    },
    0x80: {
        'addr': 0x80,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '0',
        'operand2': 'B'
    },
    0x81: {
        'addr': 0x81,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '0',
        'operand2': 'C'
    },
    0x82: {
        'addr': 0x82,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '0',
        'operand2': 'D'
    },
    0x83: {
        'addr': 0x83,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '0',
        'operand2': 'E'
    },
    0x84: {
        'addr': 0x84,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '0',
        'operand2': 'H'
    },
    0x85: {
        'addr': 0x85,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '0',
        'operand2': 'L'
    },
    0x86: {
        'addr': 0x86,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '0',
        'operand2': '(HL)'
    },
    0x87: {
        'addr': 0x87,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '0',
        'operand2': 'A'
    },
    0x88: {
        'addr': 0x88,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '1',
        'operand2': 'B'
    },
    0x89: {
        'addr': 0x89,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '1',
        'operand2': 'C'
    },
    0x8a: {
        'addr': 0x8a,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '1',
        'operand2': 'D'
    },
    0x8b: {
        'addr': 0x8b,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '1',
        'operand2': 'E'
    },
    0x8c: {
        'addr': 0x8c,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '1',
        'operand2': 'H'
    },
    0x8d: {
        'addr': 0x8d,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '1',
        'operand2': 'L'
    },
    0x8e: {
        'addr': 0x8e,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '1',
        'operand2': '(HL)'
    },
    0x8f: {
        'addr': 0x8f,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '1',
        'operand2': 'A'
    },
    0x90: {
        'addr': 0x90,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '2',
        'operand2': 'B'
    },
    0x91: {
        'addr': 0x91,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '2',
        'operand2': 'C'
    },
    0x92: {
        'addr': 0x92,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '2',
        'operand2': 'D'
    },
    0x93: {
        'addr': 0x93,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '2',
        'operand2': 'E'
    },
    0x94: {
        'addr': 0x94,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '2',
        'operand2': 'H'
    },
    0x95: {
        'addr': 0x95,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '2',
        'operand2': 'L'
    },
    0x96: {
        'addr': 0x96,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '2',
        'operand2': '(HL)'
    },
    0x97: {
        'addr': 0x97,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '2',
        'operand2': 'A'
    },
    0x98: {
        'addr': 0x98,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '3',
        'operand2': 'B'
    },
    0x99: {
        'addr': 0x99,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '3',
        'operand2': 'C'
    },
    0x9a: {
        'addr': 0x9a,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '3',
        'operand2': 'D'
    },
    0x9b: {
        'addr': 0x9b,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '3',
        'operand2': 'E'
    },
    0x9c: {
        'addr': 0x9c,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '3',
        'operand2': 'H'
    },
    0x9d: {
        'addr': 0x9d,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '3',
        'operand2': 'L'
    },
    0x9e: {
        'addr': 0x9e,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '3',
        'operand2': '(HL)'
    },
    0x9f: {
        'addr': 0x9f,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '3',
        'operand2': 'A'
    },
    0xa0: {
        'addr': 0xa0,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '4',
        'operand2': 'B'
    },
    0xa1: {
        'addr': 0xa1,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '4',
        'operand2': 'C'
    },
    0xa2: {
        'addr': 0xa2,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '4',
        'operand2': 'D'
    },
    0xa3: {
        'addr': 0xa3,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '4',
        'operand2': 'E'
    },
    0xa4: {
        'addr': 0xa4,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '4',
        'operand2': 'H'
    },
    0xa5: {
        'addr': 0xa5,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '4',
        'operand2': 'L'
    },
    0xa6: {
        'addr': 0xa6,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '4',
        'operand2': '(HL)'
    },
    0xa7: {
        'addr': 0xa7,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '4',
        'operand2': 'A'
    },
    0xa8: {
        'addr': 0xa8,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '5',
        'operand2': 'B'
    },
    0xa9: {
        'addr': 0xa9,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '5',
        'operand2': 'C'
    },
    0xaa: {
        'addr': 0xaa,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '5',
        'operand2': 'D'
    },
    0xab: {
        'addr': 0xab,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '5',
        'operand2': 'E'
    },
    0xac: {
        'addr': 0xac,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '5',
        'operand2': 'H'
    },
    0xad: {
        'addr': 0xad,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '5',
        'operand2': 'L'
    },
    0xae: {
        'addr': 0xae,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '5',
        'operand2': '(HL)'
    },
    0xaf: {
        'addr': 0xaf,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '5',
        'operand2': 'A'
    },
    0xb0: {
        'addr': 0xb0,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '6',
        'operand2': 'B'
    },
    0xb1: {
        'addr': 0xb1,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '6',
        'operand2': 'C'
    },
    0xb2: {
        'addr': 0xb2,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '6',
        'operand2': 'D'
    },
    0xb3: {
        'addr': 0xb3,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '6',
        'operand2': 'E'
    },
    0xb4: {
        'addr': 0xb4,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '6',
        'operand2': 'H'
    },
    0xb5: {
        'addr': 0xb5,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '6',
        'operand2': 'L'
    },
    0xb6: {
        'addr': 0xb6,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '6',
        'operand2': '(HL)'
    },
    0xb7: {
        'addr': 0xb7,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '6',
        'operand2': 'A'
    },
    0xb8: {
        'addr': 0xb8,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '7',
        'operand2': 'B'
    },
    0xb9: {
        'addr': 0xb9,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '7',
        'operand2': 'C'
    },
    0xba: {
        'addr': 0xba,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '7',
        'operand2': 'D'
    },
    0xbb: {
        'addr': 0xbb,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '7',
        'operand2': 'E'
    },
    0xbc: {
        'addr': 0xbc,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '7',
        'operand2': 'H'
    },
    0xbd: {
        'addr': 0xbd,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '7',
        'operand2': 'L'
    },
    0xbe: {
        'addr': 0xbe,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '7',
        'operand2': '(HL)'
    },
    0xbf: {
        'addr': 0xbf,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'RES',
        'operand1': '7',
        'operand2': 'A'
    },
    0xc0: {
        'addr': 0xc0,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '0',
        'operand2': 'B'
    },
    0xc1: {
        'addr': 0xc1,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '0',
        'operand2': 'C'
    },
    0xc2: {
        'addr': 0xc2,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '0',
        'operand2': 'D'
    },
    0xc3: {
        'addr': 0xc3,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '0',
        'operand2': 'E'
    },
    0xc4: {
        'addr': 0xc4,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '0',
        'operand2': 'H'
    },
    0xc5: {
        'addr': 0xc5,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '0',
        'operand2': 'L'
    },
    0xc6: {
        'addr': 0xc6,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '0',
        'operand2': '(HL)'
    },
    0xc7: {
        'addr': 0xc7,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '0',
        'operand2': 'A'
    },
    0xc8: {
        'addr': 0xc8,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '1',
        'operand2': 'B'
    },
    0xc9: {
        'addr': 0xc9,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '1',
        'operand2': 'C'
    },
    0xca: {
        'addr': 0xca,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '1',
        'operand2': 'D'
    },
    0xcb: {
        'addr': 0xcb,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '1',
        'operand2': 'E'
    },
    0xcc: {
        'addr': 0xcc,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '1',
        'operand2': 'H'
    },
    0xcd: {
        'addr': 0xcd,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '1',
        'operand2': 'L'
    },
    0xce: {
        'addr': 0xce,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '1',
        'operand2': '(HL)'
    },
    0xcf: {
        'addr': 0xcf,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '1',
        'operand2': 'A'
    },
    0xd0: {
        'addr': 0xd0,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '2',
        'operand2': 'B'
    },
    0xd1: {
        'addr': 0xd1,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '2',
        'operand2': 'C'
    },
    0xd2: {
        'addr': 0xd2,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '2',
        'operand2': 'D'
    },
    0xd3: {
        'addr': 0xd3,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '2',
        'operand2': 'E'
    },
    0xd4: {
        'addr': 0xd4,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '2',
        'operand2': 'H'
    },
    0xd5: {
        'addr': 0xd5,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '2',
        'operand2': 'L'
    },
    0xd6: {
        'addr': 0xd6,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '2',
        'operand2': '(HL)'
    },
    0xd7: {
        'addr': 0xd7,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '2',
        'operand2': 'A'
    },
    0xd8: {
        'addr': 0xd8,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '3',
        'operand2': 'B'
    },
    0xd9: {
        'addr': 0xd9,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '3',
        'operand2': 'C'
    },
    0xda: {
        'addr': 0xda,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '3',
        'operand2': 'D'
    },
    0xdb: {
        'addr': 0xdb,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '3',
        'operand2': 'E'
    },
    0xdc: {
        'addr': 0xdc,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '3',
        'operand2': 'H'
    },
    0xdd: {
        'addr': 0xdd,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '3',
        'operand2': 'L'
    },
    0xde: {
        'addr': 0xde,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '3',
        'operand2': '(HL)'
    },
    0xdf: {
        'addr': 0xdf,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '3',
        'operand2': 'A'
    },
    0xe0: {
        'addr': 0xe0,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '4',
        'operand2': 'B'
    },
    0xe1: {
        'addr': 0xe1,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '4',
        'operand2': 'C'
    },
    0xe2: {
        'addr': 0xe2,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '4',
        'operand2': 'D'
    },
    0xe3: {
        'addr': 0xe3,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '4',
        'operand2': 'E'
    },
    0xe4: {
        'addr': 0xe4,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '4',
        'operand2': 'H'
    },
    0xe5: {
        'addr': 0xe5,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '4',
        'operand2': 'L'
    },
    0xe6: {
        'addr': 0xe6,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '4',
        'operand2': '(HL)'
    },
    0xe7: {
        'addr': 0xe7,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '4',
        'operand2': 'A'
    },
    0xe8: {
        'addr': 0xe8,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '5',
        'operand2': 'B'
    },
    0xe9: {
        'addr': 0xe9,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '5',
        'operand2': 'C'
    },
    0xea: {
        'addr': 0xea,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '5',
        'operand2': 'D'
    },
    0xeb: {
        'addr': 0xeb,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '5',
        'operand2': 'E'
    },
    0xec: {
        'addr': 0xec,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '5',
        'operand2': 'H'
    },
    0xed: {
        'addr': 0xed,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '5',
        'operand2': 'L'
    },
    0xee: {
        'addr': 0xee,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '5',
        'operand2': '(HL)'
    },
    0xef: {
        'addr': 0xef,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '5',
        'operand2': 'A'
    },
    0xf0: {
        'addr': 0xf0,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '6',
        'operand2': 'B'
    },
    0xf1: {
        'addr': 0xf1,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '6',
        'operand2': 'C'
    },
    0xf2: {
        'addr': 0xf2,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '6',
        'operand2': 'D'
    },
    0xf3: {
        'addr': 0xf3,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '6',
        'operand2': 'E'
    },
    0xf4: {
        'addr': 0xf4,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '6',
        'operand2': 'H'
    },
    0xf5: {
        'addr': 0xf5,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '6',
        'operand2': 'L'
    },
    0xf6: {
        'addr': 0xf6,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '6',
        'operand2': '(HL)'
    },
    0xf7: {
        'addr': 0xf7,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '6',
        'operand2': 'A'
    },
    0xf8: {
        'addr': 0xf8,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '7',
        'operand2': 'B'
    },
    0xf9: {
        'addr': 0xf9,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '7',
        'operand2': 'C'
    },
    0xfa: {
        'addr': 0xfa,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '7',
        'operand2': 'D'
    },
    0xfb: {
        'addr': 0xfb,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '7',
        'operand2': 'E'
    },
    0xfc: {
        'addr': 0xfc,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '7',
        'operand2': 'H'
    },
    0xfd: {
        'addr': 0xfd,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '7',
        'operand2': 'L'
    },
    0xfe: {
        'addr': 0xfe,
        'cycles': [16],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '7',
        'operand2': '(HL)'
    },
    0xff: {
        'addr': 0xff,
        'cycles': [8],
        'flags': ['-', '-', '-', '-'],
        'length': 0x02,
        'mnemonic': 'SET',
        'operand1': '7',
        'operand2': 'A'
    }
}
