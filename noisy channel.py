import numpy as np
from noise_generator import NoiseGenerator

class NoiseChannel:
    def __init__(self):
        pass
def apply_noise_to_bits(bits, noise):
        noisy_bits = bits + noise
        return noisy_bits
 
"""testiranje suma:
input_bits = np.array([0, 1, 0, 1, 1, 0, 1, 0])  
length = len(input_bits)  
noise_generator = NoiseGenerator()
white_noise = noise_generator.generate(length)
noisy_bits = NoiseChannel()
noisy_bits = apply_noise_to_bits(input_bits, white_noise)


print("input_bits:", input_bits)
print("sum:", white_noise)
print("Bitovi s sumom:", noisy_bits)"""