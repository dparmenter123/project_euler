import sys
import unittest
from problem1 import summify, solution1, solution2

class problem1(unittest.TestCase):
    def setUp(self):
        self.data = [
            (0, 0),
            (1, 0),
            (3, 0),
            (4, 3),
            (6, 8),
            (10, 23),
            (1000, 233168)
        ]

    # test the summification
    def test_summify(self):
        self.assertEqual(summify(4, 3), 3)
        self.assertEqual(summify(7, 3), 9)
        self.assertEqual(summify(10, 3), 18)
        self.assertEqual(summify(3, 1), 3)
        self.assertEqual(summify(9, 3), 9)   # because the function is non-inclusive
        self.assertEqual(summify(10, 3), 18) # "   "
        self.assertEqual(summify(11, 5), 15)
        self.assertEqual(summify(31, 15), 45)
    
    # one line solution: compute the union of the sets of numbers divisible by 3 and 5
    def test_solution1(self):   
        for result in self.data:
            self.assertEqual(solution1(result[0]), result[1])

    # the 'paper' solution
    def test_solution2(self):
        for result in self.data:
            self.assertEqual(solution2(result[0]), result[1])
