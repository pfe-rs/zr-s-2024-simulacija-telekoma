import numpy as np


## sum može biti normalano i uniformno ras
class NoiseGenerator:
    def __init__(self, distribution='normal'):
        self.distribution = distribution

    def generate(self, length, variance=None):
        if variance is None:
            variance = np.random.uniform(0.1, 1.0)

        if self.distribution == 'normal':
            noise_samples = np.random.normal(0, np.sqrt(variance), length)
        elif self.distribution == 'uniform':
            noise_samples = np.random.uniform(-np.sqrt(3 * variance), np.sqrt(3 * variance), length)
        else:
            raise ValueError("Ne postoji taj tip šuma")

        return noise_samples

## u sustini dodaje sum
class NoisyChannel:
    def __init__(self, noise_generator):
        self.noise_generator = noise_generator

    def transmit(self, message, variance=None):
        noise = self.noise_generator.generate(len(message), variance)
        received_message = (message + noise) % 2  # jer je binarno
        return received_message.astype(int)

def nearest_angle_to_bit(values):
    angles = np.arctan2(np.sin(values), np.cos(values))
    return np.round((angles + np.pi) / (2 * np.pi)).astype(int)

## pronalazi se najbliži ugao (faza) i uporedjuje se s 1 i 0
