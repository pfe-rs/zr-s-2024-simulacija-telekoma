import matplotlib.pyplot as plt 
import numpy as np
import modulation
import math

class Mapper:
    def __init__(self, PSK = None, QAM = None):
        if PSK.isNone():
           self.QAM = QAM
        else:
            self.PSK = PSK 
        
    def split_input_bits(self, input_bits, step):
     return [input_bits[i:i+step] for i in range(0, len(input_bits), step)]

    def step(self, input_bits, step):
        if self.QAM.isNone():
            return modulation.PSK.map(self.split_input_bits(input_bits, step))
        else: 
            return modulation.QAM.map(self.split_input_bits(input_bits, step))
        
    def plot_constellation(self, input_bits):
        symbols = self.step(input_bits, math.log2(len(input_bits)))
        I_values = [symbol.I for symbol in symbols]
        Q_values = [symbol.Q for symbol in symbols]
        plt.scatter(I_values, Q_values, marker="o", color="b")
        plt.xlabel("I")
        plt.ylabel("Q")
        plt.grid(True)
        plt.show()
        
 
