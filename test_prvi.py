import pytest
import numpy as np
from simboli import Symbol
from modulation import PSK, QAM
from mapper import Mapper
from gen_suma_i_desumer import NoiseGenerator, NoisyChannel, nearest_angle_to_bit


@pytest.fixture
def psk_modulation():
    return PSK(2, 4)  

@pytest.fixture
def qam_modulation():
    return QAM(4, 16) 

@pytest.fixture
def noise_generator():
    return NoiseGenerator()

@pytest.fixture
def noisy_channel(noise_generator):
    return NoisyChannel(noise_generator)

def test_psk_modulation(psk_modulation):
    bits = np.random.randint(0, 2, 4)  
    symbol = psk_modulation.map(bits)
    assert isinstance(symbol, Symbol)


def test_qam_modulation(qam_modulation):
    bits = np.random.randint(0, 2, 16)  
    symbol = qam_modulation.map(bits)
    assert isinstance(symbol, Symbol)


def test_mapper_split_input_bits():
    mapper = Mapper(None)  
    input_bits = [0, 1, 0, 1, 1, 0, 1, 0]
    step = 2
    result = mapper.split_input_bits(input_bits, step)
    assert result == [[0, 1], [0, 1], [1, 0], [1, 0]]

def test_mapper_plot_constellation():
    mapper = Mapper(None)
    input_bits = [0, 1, 0, 1, 1, 0, 1, 0]
    with pytest.raises(AttributeError):
        mapper.plot_constellation(input_bits) 


def test_noise_generator_normal_distribution():
    noise_generator = NoiseGenerator(distribution='normal')
    noise_samples = noise_generator.generate(100)
    assert len(noise_samples) == 100

def test_noise_generator_uniform_distribution():
    noise_generator = NoiseGenerator(distribution='uniform')
    noise_samples = noise_generator.generate(100)
    assert len(noise_samples) == 100

def test_noise_generator_invalid_distribution():
    with pytest.raises(ValueError):
        noise_generator = NoiseGenerator(distribution='invalid')

def test_noisy_channel_transmit():
    noise_generator = NoiseGenerator()
    noisy_channel = NoisyChannel(noise_generator)
    message = np.random.randint(0, 2, 100) 
    received_message = noisy_channel.transmit(message)
    assert len(received_message) == len(message)

def test_nearest_angle_to_bit():
    values = np.array([0.1, 1.2, -0.3, -2.5, 3.7])
    result = nearest_angle_to_bit(values)
    assert isinstance(result, np.ndarray)
