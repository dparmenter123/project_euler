from utils import timeit
from utils import digitize, numberize, is_prime, gen_primes, rwh_primes
from math import log10
from itertools import combinations

def prime_pair(a,b):
    a_b = a * 10 ** int(log10(b)+1) + b
    if not is_prime(a_b):
        return False

    b_a = b * 10 ** int(log10(a)+1) + a
    if not is_prime(b_a):
        return False
    return True

@timeit
def solution():
    sets = []
    for prime in gen_primes():
        if prime == 2:
            continue
        for s in sets:
            ispp = all(prime_pair(element, prime) for element in s)
            if ispp:
                sets.append(s|{prime})
                if len(s) + 1 >= 4:
                    print s | {prime}
                if len(s) + 1 == 5:
                    return sum(s) + prime
        sets.append({prime})
    return None

@timeit
def solution2():
    primes = rwh_primes(1000)
    for candidate in combinations(primes, 4):
#        print candidate
        if all([prime_pair(a,b) for a,b in combinations(candidate, 2)]):
            print candidate
            return sum(candidate)


################################################################
#
################################################################
if __name__ == "__main__":
    print '\nsolution:', solution2()
