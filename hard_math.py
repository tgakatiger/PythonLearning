from collections import namedtuple
from math import log2

class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.it = iter([self.a, self.b])

    def __repr__(self):
        return f'({self.a}, {self.b})'

    def __hash__(self):
        _a = min(self.a, self.b)
        _b = max(self.a, self.b)
        return hash((_a, _b))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __lt__(self, other):
        return self.a < other.a

    def __iter__(self):
        return self.it

    def __next__(self):
        next(self.it)

class PairSum(Pair):
    def __init__(self, pair):
        super().__init__(pair.a, pair.b)
        
    def __repr__(self):
        return str(self.a + self.b)

    def __int__(self):
        return self.a + self.b


class HMSolver:
    def __init__(self, hmstruct, *args, **kwargs):
        self.item = hmstruct
        self.num = hmstruct.num

    def get_nums_set(self):
        out = set()
        for i in range(2, int(self.num ** 0.5) + 2):
            if self.num % i == 0:
                out.add(i)
                out.add(int(self.num / i))
        return sorted(tuple(out))

    def get_pairs_list(self):
        out = set()
        numbers = Numbers()
        for i in range(2, int(self.num ** 0.5) + 2):
            if self.num % i == 0:
                pair = Pair(int(i), int(self.num/i))
                if pair not in out \
                   and not numbers.all_primes_in_pair(pair) \
                   and numbers.is_even(pair.a * pair.b) \
                   and not numbers.is_even(pair.a + pair.b):
                   # and (2 in pair and all([numbers.is_even(i) for i in pair])):
                    out.add(pair)
        return sorted(list(out))

    def get_pairs_sum(self):
        out = []
        for pair in self.item.pairs:
            out.append(PairSum(pair))
        return sorted(out)


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
        

class HMTemplateBase:
    def __init__(self, template='', *args, **kwargs):
        self.template = template

    def set(self, template=None):
        if template is not None:
            self.template = template

    def __repr__(self):
        return self.template
        
        
class HMViewTemplate(HMTemplateBase):
    def __init__(self, obj=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.obj = obj
        
    def set_object(self, obj=None):
        if obj is not None:
            self.obj = obj

    def get_object(self):
        return self.obj

    def set_template(self, template):
        self.template = template
        
    def get_template(self):
        return self.template
        
    def get_instance(self):
        attr_list = [i for i in dir(self.get_object()) if not i.startswith('_')]
        out = ''
        for t_word in self.get_template().split():
            if t_word in attr_list:
                attr = self.get_object().__getattribute__(t_word)
                if isinstance(attr, int):
                    out += f'{attr:02} '
                else:
                    out += str(attr)
        return out.strip()    

    
class HMView:
    def __init__(self, items_list, hm_view_template, hm_view_logic, *args, **kwargs):
        self.answer = items_list
        self.hmvt = hm_view_template
        self.hmvl = hm_view_logic
        
    def view(self):
        for item in self.answer:
            self.hmvt.set_object(item)
            if self.hmvl.check(item):
                print(self.hmvt.get_instance())

                
class HMViewLogic:
    def check(self, item):
        number = Numbers()
        if item.pairs_len > 1: # and not number.find_in_pair_list(2, item.get_pairs()):
            return True
        return False

class HMViewAllLogic:
    def check(self, item):
        return True
    

class Numbers:
    def is_prime(self, num=None):
        if num < 2:
            return False
        if num == 2:
            return True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def can_decomposed(self, num=None):
        primes_list = [i for i in range(1, num) if self.is_prime(i)]
        for i in primes_list:
            if num - i in primes_list:
                return False
        return True

    def is_even(self, num=None):
        if num % 2 == 0:
            return True
        return False

    def is_not_even(self, num=None):
        return not self.is_even(num)

    def is_pow_of_two(self, num=None):
        l = int(log2(num))
        if num == 2 ** l:
            return True
        return False

    def check_pair_for_power(self, pair=None):
        return any([self.is_pow_of_two(num) for num in pair])

    def all_primes_in_pair(self, pair=None):
        return all([self.is_prime(num) for num in pair])

    def find_in_pair_list(self, num=None, pair_list=None):
        out_list = [nums for pairs in pair_list for nums in pairs]
        print(out_list)

    
class Goldbah:
    def __init__(self, num):
        self.num = num

    def get(self):
        number = Numbers()
        out = set()
        for i in range (2, self.num):
            if number.is_prime(i):
                remain = self.num - i
                if number.is_prime(remain):
                    out.add(Pair(i, remain))
        return list(out)


class PrimeRange:
    def __init__(self, num=None):
        self.num = num

    def decompose(self):
        remain = self.num
        out = list()
        if remain == 1: return [1]
        if remain < 1 or not isinstance(remain, int): raise TypeError
        divider = 2
        while remain != 1:
            if remain % divider == 0:
                remain = remain // divider
                out.append(divider)
                continue
            divider += 1
        return out

    
def main():
    items_list = [HMStructInit(HMStruct(i)).get() for i in range(2, 100)]
    view_template = 'num set_len pairs_len pairs pairs_sum dividers'
    
    hm_view_template = HMViewTemplate()
    hm_view_template.set_template(view_template)
    
    hm_view_logic = HMViewLogic()
    
    hm = HMView(items_list, hm_view_template, hm_view_logic)
    hm.view()

    for i in range(6, 50, 2):
        print(f'{i} {sorted(Goldbah(i).get())} <=> {PrimeRange(i).decompose()}')


main()
