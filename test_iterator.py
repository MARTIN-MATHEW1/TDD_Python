import unittest
from Iterator_Example import *

class TestSquareFunctionWithIter(unittest.TestCase):

    def test_zero_max(self):
        sq = square_function_with_iter(max=0)
        result = list(sq)
        self.assertEqual(result, [1])

    def test_positive_max(self):
        sq = square_function_with_iter(max=3)
        result = list(sq)
        # print(result)
        self.assertEqual(result, [1, 2, 4, 8])

    def test_negative_max(self):
        sq = square_function_with_iter(max=-2)
        result = list(sq)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
