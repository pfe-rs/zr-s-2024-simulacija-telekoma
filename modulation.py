import numpy as np 
import math
from simboli import Symbol

class modulation:
    def __init__(self, qm=None, bit_number=None):
        if qm is None:
            self.bit_number = bit_number
            qm = math.log2(bit_number) 
        if bit_number is None:
            self.qm = qm 
            self.bit_number = 2**qm 

    def map (self):
        return 
    
class PSK(modulation):
    def map(self, bits):
        binary_string = "".join(str(bit) for bit in bits)
        num = int(binary_string, 2)
        phase_offset = 0 
        symbol_map = np.exp(1j * (2 * np.pi / self.bit_number) * np.arange(self.bit_number) + phase_offset)
        symbols = symbol_map[num]
        return Symbol(I=symbols.real, Q=symbols.imag)
       

class QAM(modulation):
    def map(self, bits):
        binary_string = "".join(str(bit) for bit in bits)
        num = int(binary_string, 2)
        side_lenght = self.qm 
        edge = side_lenght-1
        return Symbol(I=(num//side_lenght)*2-edge, Q=(num%side_lenght)*2-edge)


        