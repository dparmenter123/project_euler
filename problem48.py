import sys
from utils import timeit
from utils import digitize, numberize

def squares(MAX):
    i = 1
    while i <= MAX:
        yield i ** i
        i += 1

@timeit
def solution():
    '''
      closed form solution to the same problem
      
      Note: MAX is non-inclusive
    '''
    total = sum(squares(1000))
    return numberize(digitize(total)[-10:])

    return 0

if __name__ == "__main__":
    print solution()
