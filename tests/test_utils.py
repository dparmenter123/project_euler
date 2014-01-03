import sys
import unittest
from utils import rwh_primes

class problem1(unittest.TestCase):
    # test rwh primes
    def test_rwh_primes(self):
        primes = rwh_primes(10)
        self.assertEqual([2, 3, 5, 7], primes)
        primes = rwh_primes(20)
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19], primes)

