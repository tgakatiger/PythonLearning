from collections import namedtuple

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
        for i in range(2, int(self.num ** 0.5) + 2):
            if self.num % i == 0:
                pair = Pair(int(i), int(self.num/i))
                if pair not in out and 2 not in pair:
                    out.add(pair)
        return sorted(list(out))

    def get_pairs_sum(self):
        out = []
        for pair in self.item.pairs:
            out.append(PairSum(pair))
        return sorted(out)

    def is_even(self):
        if self.num % 2 == 0:
            return True
        return False


class HMStructInit:
    def __init__(self, hmstruct):
        self.hms = hmstruct
        hmsolver = HMSolver(self.hms)
        self.hms.set = hmsolver.get_nums_set()
        self.hms.set_len = len(self.hms.set)
        self.hms.pairs = hmsolver.get_pairs_list()
        self.hms.pairs_len = len(self.hms.pairs)
        self.hms.pairs_sum = hmsolver.get_pairs_sum()

    def get(self):
        return self.hms

    
class HMStruct:
    def __init__(self, num):
        self.num = num
        self.set = None
        self.pairs = None
        

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
        prime = Primes()
        if item.pairs_len > 1 and not prime.is_prime(item.num) \
           and not all([prime.can_decomposed(i) for i in [int(j) for j in HMSolver(item).get_pairs_sum()]]):
            return True
        return False

class HMViewAllLogic:
    def check(self, item):
        return True
    

class Primes:
    def is_prime(self, num=None):
        for i in range(2, int(num ** 0.5) + 2):
            if num % i == 0:
                return False
        return True

    def can_decomposed(self, num=None):
        primes_list = [i for i in range(1, num) if self.is_prime(i)]
        for i in primes_list:
            if num - i in primes_list:
                return False
        return True
    
    
def main():
    items_list = [HMStructInit(HMStruct(i)).get() for i in range(2, 100)]
    view_template = 'num set_len pairs_len pairs pairs_sum'
    
    hm_view_template = HMViewTemplate()
    hm_view_template.set_template(view_template)
    
    hm_view_logic = HMViewLogic()
    
    hm = HMView(items_list, hm_view_template, hm_view_logic)
    hm.view()


main()
