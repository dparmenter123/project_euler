import sys
import unittest
from problem54 import *

class problem54(unittest.TestCase):
    def setUp(self):
        self.hands = {
            'royal_flush'     : [(10,'C'),(11,'C'),(12,'C'),(13,'C'),(14,'C')],
            'straight_flush'  : [( 9,'C'),(10,'C'),(11,'C'),(12,'C'),(13,'C')],
            'four_of_a_kind'  : [( 9,'C'),( 9,'S'),( 9,'H'),( 9,'D'),(13,'C')],
            'full_house'      : [( 9,'C'),( 9,'S'),( 9,'H'),( 8,'D'),( 8,'C')],
            'flush'           : [(2, 'C'),(11,'C'),(12,'C'),(13,'C'),(14,'C')],
            'straight'        : [( 9,'D'),(10,'C'),(11,'C'),(12,'C'),(13,'C')],
            'three_of_a_kind' : [( 9,'C'),( 9,'S'),( 9,'H'),( 8,'D'),( 7,'C')],
            'two_pair'        : [( 9,'C'),( 9,'S'),( 7,'H'),( 8,'D'),( 8,'C')],
            'one_pair'        : [( 9,'C'),( 9,'S'),( 7,'H'),( 8,'D'),( 6,'C')],
            'garbage'         : [( 2,'C'),( 9,'S'),( 7,'H'),( 8,'D'),( 6,'C')],
            }

    # test the summification
    def test_hands(self):
        hands = [
            (royal_flush,     'royal_flush'),
            (straight_flush,  'straight_flush'),
            (four_of_a_kind,  'four_of_a_kind'),
            (full_house,      'full_house'),
            (flush,           'flush'),
            (straight,        'straight'),
            (three_of_a_kind, 'three_of_a_kind'),
            (two_pair,        'two_pair'),
            (one_pair,        'one_pair'),
            ]
        for func, key in hands:
            self.assertEqual(1, func(self.hands[key]))

    def test_tiebreakers(self):
        self.assertEqual(11,
                         high_triple([(10,'C'),(11,'C'),(11,'C'),(11,'C'),(14,'C')]))
        self.assertEqual(11,
                         high_pair([(10,'D'),(10,'C'),(11,'D'),(11,'C'),(14,'C')]))
        self.assertEqual(10,
                         low_pair([(10,'D'),(10,'C'),(11,'D'),(11,'C'),(14,'C')]))
        self.assertEqual(14,
                         high_card_excluding_pairs([(10,'D'),(10,'C'),(11,'D'),(11,'C'),(14,'C')]))
        self.assertEqual(14,
                         high_card([(7,'D'),(10,'C'),(9,'D'),(11,'C'),(14,'C')]))

    def test_solution(self):   
        pass
