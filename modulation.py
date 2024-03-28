import numpy as np 

class modulation:
    def __init__(self, qm, bit_number):
        self.qm = qm  
        self.bit_number = bit_number 
    
    def map (self):
        return 
    
class PSK(modulation):
    def map(self, bits):
        modulation_order=2**self.qm
        phase_offset = 0 
        symbol_map = np.exp(1j * (2 * np.pi / modulation_order) * np.arange(modulation_order) + phase_offset)
        symbols = symbol_map[bits]
        return symbol(symbols.real, symbols.imaginary)

class QAM(modulation):
    def map(self, bits)
        modulation_order=2**self.qm
        side_length = int(np.sqrt(modulation_order))
        symbol_map = np.linspace(-1 + 1j, 1 - 1j, side_length)
        symbols = symbol_map[bits]
        return symbol(symbols.real, symbols.imaginary)


        