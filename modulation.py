import numpy as np 
import math
import simboli

class modulation:
    def __init__(self, qm=None, bit_number=None):
        if qm.isNone():
            self.bit_number = bit_number
            self.qm = math.log2(bit_number)
        if bit_number.isNone():
            self.qm = qm 
            self.bit_number = 2**qm

    3
    def map (self):
        return 
    
class PSK(modulation):
    def map(self, bits):
        phase_offset = 0 
        symbol_map = np.exp(1j * (2 * np.pi / self.bit_number) * np.arange(self.bit_number) + phase_offset)
        symbols = symbol_map[bits]
        return symbol(symbols.real, symbols.imaginary)

class QAM(modulation):
    def map(self, bits):
        side_length = int(np.sqrt(self.bit_number))
        symbol_map = np.linspace(-1 + 1j, 1 - 1j, side_length)
        symbols = symbol_map[bits]
        return symbol(symbols.real, symbols.imaginary)


        