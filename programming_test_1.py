import unittest

def cut(s):
    ''' return the cut point in s '''
    if len(s) <= 1:
        return 0
    if s[-1] > s[0]:
        return 0
    if len(s) == 2:
        return 1

    mid = len(s)/2
    left = cut(s[:mid])
    right = cut(s[mid:])
    if left == 0:
        return mid + right
    else:
        return left


class Tests(unittest.TestCase):
    def test_cut(self):
        self.assertEqual(0, cut([3,4]))
        self.assertEqual(0, cut([3]))
        self.assertEqual(1, cut([5,4]))
        self.assertEqual(0, cut([1,2,3,4,6]))
        self.assertEqual(4, cut([4,5,6,7,1,2,3]))
        self.assertEqual(1, cut([7, 1,2,3,4,6]))
        


def main():
    pass

if __name__ == '__main__':
    unittest.main()
