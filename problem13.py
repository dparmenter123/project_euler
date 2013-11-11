"""
    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""
from utils import timeit

################################################################
#
################################################################

@timeit
def solution1():
    '''
    one line, completely naive solution

    this solution naively adds up all of the integers all the way to the 1's place.
    it also relies on Python having great support for big integers
    '''

    # 1) read the file
    # 2) split on the newlines
    # 3) in a list comprehension, make a list of each line of the file converted to an integer
    #    put another way, make a list of integers
    # 4) sum the list
    # 5) convert that to a string
    # 6) take the leading 10 digits

    #                               +----1---------------------+
    #                               +----2----------------------------------+
    #              +---3-----------------------------------------------------+
    #         +-4-------------------------------------------------------------+
    #      +-5-----------------------------------------------------------------+
    #                                                                          +-6-+
    return str(sum([int(x) for x in open('problem13.dat').read().split('\n')]))[:10]

################################################################
#
################################################################

@timeit
def solution2():
    '''
     Slightly clearer, more efficient solution.
     
     We know that we need only add up the first 12 digits:
     Proof: the largest number each line could possibly be is 50 consecutive 9's
            the carry from the 1's digit in the case would be 45. But the next digit
            would also be all 9's, so the 5 will not contribute to the carry.
            The 100's digit will also be all nines, so we will add its 5 plus the 4 from the 
            ones place, maxing out at 9. So, you can never have a contribution from more 
            than 2 digits back, FOR THIS PARTICULAR problem.
    '''

    total = 0
    # with open syntax will close the file cleanly
    with open('problem13.dat') as f:
        # we know it is an ascii file with newline terminators
        for line in f.readlines():
            # we know we only need the leading 12 digits, since the strings
            # are all the same length and there are only 50 of them
            total += int(line[:12])
    return str(total)[:10]

################################################################
#
################################################################

if __name__ == "__main__":
    print '\none line solution #1:', solution1()
    print '\nmore explicit solution #2:', solution2()
