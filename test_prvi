import numpy as np
from modulation import modulation, PSK, QAM
from mapper import Mapper

psk_mod = PSK(qm=1, bit_number=2)
qam_mod = QAM(qm=2, bit_number=4)
mapper_psk = Mapper(psk_mod)
mapper_qam = Mapper(qam_mod)


input_bits = [0, 1, 0, 1]  


mapper_psk.plot_constellation(input_bits)
mapper_qam.plot_constellation(input_bits)
