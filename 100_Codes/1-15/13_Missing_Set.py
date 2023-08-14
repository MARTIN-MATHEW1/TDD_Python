# Given two sets of numbers, write a Python program to find the missing numbers 
# in the second set as compared to the first and vice versa. Use the Python set. 

import unittest

def find_missing_numbers(set1, set2):
    missing_in_set1 = set2 - set1
    missing_in_set2 = set1 - set2
    return missing_in_set1, missing_in_set2

class TestFindMissingNumbers(unittest.TestCase):

    def test_missing_in_set1(self):
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        missing_set1, _ = find_missing_numbers(set1, set2)
        self.assertEqual(missing_set1, {5, 6})

    def test_missing_in_set2(self):
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        _, missing_set2 = find_missing_numbers(set1, set2)
        self.assertEqual(missing_set2, {1, 2})

    def test_no_missing_numbers(self):
        set1 = {1, 2, 3}
        set2 = {1, 2, 3}
        missing_set1, missing_set2 = find_missing_numbers(set1, set2)
        self.assertEqual(missing_set1, set())
        self.assertEqual(missing_set2, set())

if __name__ == "__main__":
    unittest.main()
