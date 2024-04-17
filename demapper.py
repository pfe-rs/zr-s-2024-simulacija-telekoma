import numpy as np
import math
from mod_s_dem import modulation
from mod_s_dem import PSK
from mod_s_dem import QAM

class Demapper:
    def __init__(self, modulation):
        self.modulation = modulation

    def step(self, symbols):
        return self.modulation.demap(symbols)

class PSKDemapper(Demapper):
    def __init__(self, modulation):
        super().__init__(modulation)

    def step(self, symbols):
        return self.modulation.demap(symbols)

class QAMDemapper(Demapper):
    def __init__(self, modulation):
        super().__init__(modulation)

    def step(self, symbols):
        return self.modulation.demap(symbols)
