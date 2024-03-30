import numpy as np

class NoiseGenerator:
    def __init__(self):
        pass

    def generate(self, length, variance=None):
        
        if variance is None:
            variance = np.random.uniform(0.1, 1.0)  
        
        noise_samples = np.random.normal(0, np.sqrt(variance), length)
        return noise_samples






