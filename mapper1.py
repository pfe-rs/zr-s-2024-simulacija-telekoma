import matplotlib.pyplot as plt 
import numpy as np
import modulation
import math
import simboli

class Mapper:
    def __init__(self, modulation):
        self.modulation = modulation  
   
    def split_input_bits(self, input_bits, step):
     return [input_bits[i:i+step] for i in range(0, len(input_bits), step)]

    def step(self, input_bits, step):
        words_array = self.split_input_bits(input_bits, step)
        if self.modulation == 'PSK':    
            return [modulation.PSK(qm = step).map(word) for word in words_array]
        else:
            return [modulation.QAM(qm = step).map(word) for word in words_array]
        

    def plot_constellation(self, input_bits, Qm):
        symbols = self.step(input_bits, Qm)
        I_values = [symbol.I for symbol in symbols]
        Q_values = [symbol.Q for symbol in symbols]
        plt.scatter(I_values, Q_values, marker="o", color="b")
        plt.xlabel("I")
        plt.ylabel("Q")
        plt.grid(True)
        plt.show()
        
 
