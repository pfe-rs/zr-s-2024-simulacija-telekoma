import matplotlib.pyplot as plt 
import numpy as np

class Mapper:
    def __init__(self, modulation):
        self.modulation = modulation
        
    def split_input_bits(self, input_bits, step):
     return [input_bits[i:i+step] for i in range(0, len(input_bits), step)]

    def step(self, input_bits, step):
        return self.split_input_bits(input_bits, step)
    def plot_constellation(self, input_bits):
        input_bits_str = ''.join(map(str, input_bits)) 
        symbols = self.modulation.modulate(input_bits_str)
        plt.scatter(np.real(symbols), np.imag(symbols), color='b')
        plt.title(f'{self.modulation.modulation_type} Konstalacija')
        plt.xlabel('I')
        plt.ylabel('Q')
        plt.grid(True)
        plt.show()
 

