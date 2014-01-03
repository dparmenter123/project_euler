from utils import timeit
from utils import rwh_primes

MAX = 100

@timeit
def solution():
    primes = rwh_primes(MAX)
    prime_set = set(primes)

    # precompute the totals, we want to do this only once
    totals = [sum(primes[0:i+1]) for i in range(len(primes))]

    # for each possible starting spot...
    for i in range(len(primes)):

        # figure out the effective total. delta is subtracted from each 
        # pre-computed total
        if i == 0:
            delta = 0
        else:
            delta = totals[i-1]
        

def solution1():
    # 
    primes = rwh_primes(MAX)
    prime_set = set(primes)
    start = 0
    end = 0
    best = (0, 0)
    for i in range(len(primes)):
        total = sum(primes[0:start+1])
        delta = primes[i] - primes[0]
        for j, p in enumerate(primes[start:]):
            total += (p - delta)
            total2 = sum(primes[i:j+start+1])
            if total > MAX:
                break
            if total in prime_set:
                end = j + start + 1
                print '*', i, end, total
        if (end-i) > (best[1]-best[0]):
            best = (i, end)
        start = end
        print '***', best, sum(primes[best[0]:best[1]])
#        if i > 3:
#            break
    return sum(primes[best[0]:best[1]+1])

def solution2():
    best = 0
    primes = rwh_primes(MAX)
    for i in range(len(primes)):
        for j in range(i, len(primes), 1):
            t = sum(primes[i:j])
            if t in primes and j-i>best:
                print j-i, primes[i], primes[j], sum(primes[i:j])
                best = j-i
            

################################################################
#
################################################################
if __name__ == "__main__":
    print '\nsolution:', solution()
