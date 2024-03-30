import numpy as np
from noise_generator import NoiseGenerator

class NoiseChannel:
    def __init__(self):
        pass
def apply_noise_to_bits(bits, noise):
        noisy_bits = bits + noise
        return noisy_bits
