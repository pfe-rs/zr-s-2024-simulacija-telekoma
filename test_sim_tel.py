import pytest
import numpy as np
from modulation import PSK, QAM
from mapper import Mapper

@pytest.fixture
def random_bits():
    return np.random.randint(2, size=100)
 
def test_psk_modulation(random_bits):
    psk_mod = PSK(8)
    symbols = psk_mod.modulate("".join(map(str, random_bits)))
    assert len(symbols) == len(random_bits) // 3 

def test_qam_modulation(random_bits):
    qam_mod = QAM(16)
    symbols = qam_mod.modulate("".join(map(str, random_bits)))
    assert len(symbols) == len(random_bits) // 4 


def test_mapper_plot_constellation(random_bits):
    psk_mod = PSK(8)
    qam_mod = QAM(16)
    
    mapper_psk = Mapper(psk_mod)
    mapper_psk.plot_constellation(random_bits)

    mapper_qam = Mapper(qam_mod)
    mapper_qam.plot_constellation(random_bits)

test_psk_modulation(random_bits())
test_qam_modulation(random_bits())
test_mapper_plot_constellation(random_bits())