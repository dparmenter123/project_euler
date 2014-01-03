import sys
from utils import timeit
import utils
from math import sqrt, ceil, floor

"""
Goldbach's other conjecture
Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}  

    # The running integer that's checked for primeness
    q = 2  

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q        
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

def composites():
    gp = gen_primes()
    gp.next() # skip 2
    previous = gp.next()
    for prime in gp:
        for composite in range(previous+2, prime, 2):
            yield composite
        previous = prime


def double_squares(start):
    ''' return all the double squares greater than low, and less than or equal to high'''
    x = int(ceil(sqrt(start/2)))
    x = max(x, 1)
    while True:
        yield 2 * x ** 2
        x += 1

def solution():
    # prime generator
    pg = gen_primes()
    pg.next() # skip 2&3
    pg.next() # skip 2&3

    # results is a dictionary with the largest sum we've seen for each prime
    # prime the pump with the the sum of the first prime and the sum of it + the first double
    results = {}
    results[3] = 3

    # also keep track of all the primes we've seen so far, in order
    primes = [3]

    # and keep track of all the sums we've seen. This this the most important optimization
    sums = set([5])

    # for each composite
    for composite in composites():
#        print '----------------------------------------------------------------'
#        print 'composite: ', composite
        # if we've seen it, great, that's kind of the point
        seen = False
        if composite in sums:
            # we've already seen this, this is the key optimization
            seen = True
        else:
            # we haven't seen this composite before, so ...
            # add in any primes that are smaller than this composite
            while primes[-1] < composite:
                prime = pg.next()
                primes.append(prime)
                results[prime] = 0
            # now walk down the list of primes
            for prime in primes:
                # what is the current largest sum for this prime?
                largest = results[prime]
                if largest < composite:
                    # check all the double squares that we haven't seen yet
                    for ds in double_squares(max(largest - prime, 0)):
                        results[prime] = prime + ds
                        # add this to the cache
                        sums.add(prime+ds)

                        # if this is true, we've found what we're looking for, but we complete the 
                        # loop for completeness
                        if composite == prime + ds:
                            seen = True
                        elif prime + ds > composite:
                            # we've overshot, so we can stop this iteration
                            break
            if not seen:
                return composite
    return 0

################################################################
#
################################################################

if __name__ == "__main__":
#     for prime in gen_primes():
#         for ds in double_squares(1):
#             print '%d + %d == %d' % (prime, ds, prime + ds)
#             if prime + ds > 123:
#                 break
#         if prime > 123:
#             break
    print '\nsolution:', solution()
