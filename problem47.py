from utils import rwh_primes, digitize, numberize
from collections import defaultdict

MAX = 1000000
PRIMES = rwh_primes(MAX)
MEMO = defaultdict(set)
for p in PRIMES:
    MEMO[p] = set([p])

def factor4(x):
    orig = x
    for p in PRIMES:
        if x % p == 0:
            x /= p
            break
    MEMO[orig] = MEMO[x] | set([p])
    return len(MEMO[orig]) == 4

def solution():
    n = 2
    print 'starting ...'
    while True:
        if factor4(n):
            if factor4(n+1):
                if factor4(n+2):
                    if factor4(n+3):
                        return n
                    else:
                        n += 4
                else:
                    n += 3
            else:
                n += 2
        else:
            n += 1
#        if n % 1000 == 0:
#            print n
        if n > MAX:
            break

                

if __name__ == "__main__":
    print solution()
