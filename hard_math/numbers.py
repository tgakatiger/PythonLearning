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
