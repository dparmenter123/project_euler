from utils import timeit, gen_primes
from math import sqrt

def gen_dimensions():
    d = 3
    while True:
        yield d
        d += 2

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

@timeit
def solution():
    primes = 0
    composites = 0
    gp = gen_primes()
    gp.next()
    prime = gp.next()

    N = 1
    while True:
        # for each square
        for square in gen_dimensions():
            ur = N + square - 1
            ul = ur + square - 1
            lr = ul + square - 1
            N = lr + square - 1
            for corner in (ur, ul, lr):
                if is_prime(corner):
                    primes += 1
                else:
                    composites += 1
            composites += 1
            #
            # matching = 0
            # while prime < N:
            #     if prime in (ul, ur, lr):
            #         matching += 1
            #     prime = gp.next()
            # primes += matching
            # composites += (4 - matching)
            ratio = float(primes) / (primes + composites)
#            print ratio
            if ratio < 0.1:
                return square

    return 2

@timeit
def solutionx():
    corner_primes = 0
    side_primes = 0
    last_prime = 0
    gp = gen_primes()
    gp.next()
    last_prime = gp.next() 

    # forever
    N = 1
    while True:
        # for each square
        for square in gen_dimensions():
            # for each side
            for side in range(4):
                # for each element on the side
                for element in range(1, square):
                    # increment the global number
                    N += 1
                    # see if we need a new prime
                    if N > last_prime:
                        last_prime = gp.next()
                    # if we find a prime, it is either a side or a corner
                    if N == last_prime:
                        if element < square - 1:
                            side_primes += 1
                        else:
                            corner_primes += 1
            
            # are we done
            ratio = float(corner_primes) / (corner_primes + side_primes)
            if ratio < 0.1:
                return square
        

    return None

################################################################
#
################################################################
if __name__ == "__main__":
    print '\nsolution:', solution()
