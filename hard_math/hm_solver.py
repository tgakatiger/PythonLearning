from numbers import Numbers, Pair, PairSum

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
