'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

from utils import timeit
from itertools import permutations
from itertools import product

def begins(prefix, sequence):
    '''
     Test a given sequence to see if the prefix is found at the beginning
    '''
    if len(prefix) > len(sequence):
        return False
    for i, p in enumerate(prefix):
        if sequence[i] != p:
            return False
    return True

def numberize(digits):
    '''
     Take a sequence and multiply it back together to form a number
    '''
    result = 1/10
    for digit in digits:
        result = result * 10 + digit
    return result

def digitize(N):
    '''
     Take the given number and return it as a list of digits
    '''
    result = []
    if N == 0:
        return [0]
    while N > 0:
        result.append(N % 10)
        N /= 10
    result.reverse()
    return result
        
def test_candidate(candidate, prefix):
    '''
     test this candidate with this prefix
    '''

    # work thru the candidate, starting with 1 * the prefix, etc
    remainder = candidate

    # N cannot be 9 or greater, not sure how to prove the max of N, take 8 for now
    for i in range(1, 9, 1):
        # take the prefix and multiply it by the current number in the sequence
        prefix2 = digitize(i*numberize(prefix))
        if not begins(prefix2, remainder):
            # if it doesn't match our current place, we're done
            return False
        remainder = remainder[len(prefix2):]
        if len(remainder) == 0:
            # it all matched, we're done
            return True
    # this should never happen
    raise Exception    

@timeit
def solution():
    '''
     Plan: generating 
    '''

    # generate all possible pandigitals, largest to smallest
    for candidate in permutations(range(9, 0, -1)):
        # each pandigital had been digitized, so it is a sequence of the digits
        for i in range(1,9,1):
            # now we generate the 8 possible prefixes of this number
            # we can do this because we know we multiply by 1 first, 
            # so we can eliminate any candidate that is not a prefix
            prefix = candidate[:i]
            # and see if this number actually works
            if test_candidate(candidate, prefix):
                # we've found it! Since we started with the largest, we're done
                return numberize(candidate)
    return None

################################################################
#
################################################################
if __name__ == "__main__":
    print '\nsolution:', solution()
