import time                                                
import logging

################################################################
# logging
#
# TODO: move logging configuration into a separate file

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

################################################################
# timer

def timeit(method):
    '''
     decorator for timing methods

     output goes to logger at the INFO level.

     http://www.andreas-jung.com/contents/a-python-decorator-for-...
     ...measuring-the-execution-time-of-methods

     '''
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        logger.info('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te-ts))
        return result

    return timed

################################################################
# rwh_primes
# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188

def rwh_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

################################################################
def numberize(digits):
    '''
     Take a sequence and multiply it back together to form a number
    '''
    result = 1/10
    for digit in digits:
        result = result * 10 + digit
    return result

################################################################
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
        

################################################################
# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes(start=2):
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
            if q >= start:
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

################################################################

def is_prime(n):
    ''' fast test for primality'''

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
