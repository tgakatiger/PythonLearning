from numbers import Numbers

class HMViewLogic:
    def __init__(self, *args, **kwargs):
        pass
    
    def check(self, item):
        number = Numbers()
        if item.pairs_len > 1: # and not number.find_in_pair_list(2, item.get_pairs()):
            return True
        return False

class HMViewAllLogic:
    def check(self, item):
        return True
