import sys
import unittest
from problem59 import compute_score

class problem59(unittest.TestCase):
    def setUp(self):
        pass

    def test_score(self):
        self.assertEqual(compute_score(''), 0)
        self.assertEqual(compute_score('This is the day'), 1)
        self.assertEqual(compute_score('The be all and end all'), 3)
        self.assertEqual(compute_score('And AND and.AnD'), 4)
        self.assertEqual(compute_score('(And) I was the one!'), 3)

