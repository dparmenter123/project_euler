import sys
import unittest
from problem38 import begins, numberize, digitize

class problem38(unittest.TestCase):
    def setUp(self):
        pass

    def test_begins(self):
        self.assertTrue(begins([1,], [1]))
        self.assertTrue(begins([1,], [1,2]))
        self.assertTrue(begins([1,], [1,2,3,4]))
        self.assertTrue(begins([1,2,3,4], [1,2,3,4]))
        self.assertFalse(begins([1,2,3,4,5], [1,2,3,4]))
        self.assertFalse(begins([1,], [9,2,3,4]))
        self.assertFalse(begins([1,], []))

    def test_digitize(self):
        self.assertEqual(digitize(0), [0])
        self.assertEqual(digitize(1), [1])
        self.assertEqual(digitize(12), [1,2])
        self.assertEqual(digitize(987654321), [9,8,7,6,5,4,3,2,1])

    def test_numberize(self):
        self.assertEqual(numberize([1]), 1)
        self.assertEqual(numberize([1,2]), 12)
        self.assertEqual(numberize([0]), 0)

    def test_stability(self):
        for N in range(1000):  
            self.assertEqual(numberize(digitize(numberize(digitize(N)))), N)

    
