import sys
from utils import timeit
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

      http://projecteuler.net/problem=1
"""

################################################################
# utility function that computes the sum of all numbers from 
# modulus, counting by modulus, upto but NOT including the modulus
################################################################

def summify(MAX, modulus):
    '''
     find the sum of all numbers in a range, with a given modulus
    '''
    # make it be non-inclusive
    if MAX == 0:
        return 0
    MAX -= 1 

    # basic algo is to find the pairs

    # (no pairs)
    # 3
    
    # (1 pair)
    # 3 6
    # +-+
    
    # (1 pair + 1 extra)
    # 3 6 9 
    # +-x-+ 

    # (2 pairs)
    # 3 6 9 12
    # | +-+  |
    # +------+ 

    # (2 pairs + 1 extra)
    # 3 6 9 12 15
    # | | x  |  |
    # | +----+  |
    # +---------+

    # find the midpoint
    # e.g. maximum = 3 * (1000 / 3 ) ==> 999
    #      min     = 3
    #      mid     = 501
    maximum  = modulus * (MAX / modulus) 
    minimum  = modulus
    midpoint = (maximum + minimum) / 2.0 # use float to preserve non-integral values

    # how many points are to the left of the midpoint?
    pairs = 0
    extra = 0
    if int(midpoint) == midpoint:
        pairs = midpoint/modulus - 1
        extra = midpoint
    else:
        pairs = midpoint/modulus - 0.5

    # each pair totals to the size of the outermost pair: max + min
    # then include the midpoint, if need be
    total = pairs * (maximum + minimum) + extra
    return int(total)

################################################################
#
################################################################

@timeit
def solution1(MAX):
    '''
      one line solution to project euler problem 1
      
      Note: MAX is non-inclusive
    '''    
    return sum(set(range(3, MAX, 3)) | set(range(5, MAX, 5)))

################################################################
#
################################################################

@timeit
def solution2(MAX):
    '''
      closed form solution to the same problem
      
      Note: MAX is non-inclusive
    '''
    return summify(MAX, 3) + summify(MAX, 5) - summify(MAX, 15)

################################################################
#
################################################################

if __name__ == "__main__":
    print '\nset-based solution:', solution1(1000)
    print '\nclosed form solution:', solution2(1000)
    
    print '\nset-based solution on much larger input:', solution1(100000000)
    print '\nclosed form solution on much larger input:', solution2(100000000)
