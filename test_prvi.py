
from modulation import modulation
from modulation import  PSK
from modulation import QAM
from mapper import Mapper
input_bits = [0, 1, 1, 0, 1, 0, 1, 1]  
mapper_psk = Mapper(modulation_type='PSK', bit_number=8)  
mapper_psk.plot_constellation(input_bits)

mapper_qam = Mapper(modulation_type='QAM', bit_number=16)  
mapper_qam.plot_constellation(input_bits)
