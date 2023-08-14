#  Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set

import unittest

def find_max_product_pair(numbers):
    if len(numbers) < 2:
        return None

    max_num = max(numbers)
    numbers.remove(max_num)
    second_max_num = max(numbers)

    return max_num, second_max_num

class TestFindMaxProductPair(unittest.TestCase):

    def test_max_product_pair(self):
        numbers = [1, 3, 5, 2, 4]
        max_num, second_max_num = find_max_product_pair(numbers)
        self.assertEqual(max_num * second_max_num, 20)

    def test_single_number(self):
        numbers = [3]
        result = find_max_product_pair(numbers)
        self.assertIsNone(result)

    def test_empty_list(self):
        numbers = []
        result = find_max_product_pair(numbers)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
