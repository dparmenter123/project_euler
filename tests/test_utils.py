import sys
import unittest
from utils import rwh_primes, gen_primes, is_prime

class Test(unittest.TestCase):
    def test_rwh_primes(self):
        primes = rwh_primes(10)
        self.assertEqual([2, 3, 5, 7], primes)
        primes = rwh_primes(20)
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19], primes)

    def test_gen_primes(self):
        gp = gen_primes()
        self.assertEqual([2,3,5,7,11], [gp.next() for i in range(5)])

    def test_gen_primes_start(self):
        gp = gen_primes(6)
        self.assertEqual([7,11,13,17,19], [gp.next() for i in range(5)])

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(109))
        self.assertTrue(is_prime(673))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(999))
