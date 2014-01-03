from utils import timeit
from utils import gen_primes, digitize, numberize
from itertools import combinations
import collections
from collections import defaultdict

def make_keys(digits, digit):
    # return all the hash keys for this set of digits + repeated digit

    # find the places where this digit is repeated
    # e.g. [9,8,1,1,2] => (2,3)
    places = [x for x,y in enumerate(digits) if y == digit]

    # generate all of the pairwise combinations
    # e.g. (2,3,5) ==> (2,3), (2,5), (3,5), (2,3,5)
    results = []
    for l in range(2, len(places) + 1, 1):
        for combo in combinations(places, l):
            result = ''
            for x,y in enumerate(digits):
                if x in combo:
                    result += '*'
                else:
                    result += '%d' % y
            results.append(result)
    return results

def repeated_digits(digits):
    return [x for x, y in collections.Counter(digits).items() if y > 1]

def candidates():
    for p in gen_primes():
        digits = digitize(p)
        if len(digits) > len(set(digits)):
            yield digits

@timeit
def solution():
    results = defaultdict(list)
    for c in candidates():
        digits = repeated_digits(c)
        for digit in digits:
            for key in make_keys(c, digit):
                results[key].append(numberize(c))
                if len(results[key]) >= 7:
                    print len(results[key]), key, results[key]
                    if len(results[key]) > 7:
                        return sorted(results[key])[0]
    return 0            

################################################################
#
################################################################
if __name__ == "__main__":
    print '\nsolution:', solution()
