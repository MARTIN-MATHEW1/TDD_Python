# Write a Python program to check if a set is a subset of another set.
import unittest

def check_subset(main_set, check_set):
    return check_set.issubset(main_set)

class CheckSubset (unittest.TestCase):


    def test_subset(self):
        set1 = {1, 2}
        set2 = {1, 2, 3, 4}
        self.assertTrue(check_subset(set2, set1))

    def test_not_subset(self):
        set1 = {5, 6}
        set2 = {1, 2, 3, 4}
        self.assertFalse(check_subset(set2, set1))

if __name__ == "__main__":
    unittest.main()
