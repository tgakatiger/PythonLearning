from numbers import PrimeRange
from hm_solver import HMSolver


class HMStructInit:
    def __init__(self, hmstruct):
        self.hms = hmstruct
        hmsolver = HMSolver(self.hms)
        self.hms.set = hmsolver.get_nums_set()
        self.hms.set_len = len(self.hms.set)
        self.hms.pairs = hmsolver.get_pairs_list()
        self.hms.pairs_len = len(self.hms.pairs)
        self.hms.pairs_sum = hmsolver.get_pairs_sum()
        self.hms.dividers = PrimeRange(self.hms.num).decompose()

    def get(self):
        return self.hms

    
class HMStruct:
    def __init__(self, num):
        self.num = num
        self.set = None
        self.pairs = None

    def get_pairs(self):
        return self.pairs
