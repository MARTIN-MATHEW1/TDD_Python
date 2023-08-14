# Write a Python program to convert a given list of tuples to a list of lists.


import unittest

def convert_to_list_of_lists(tuple_list):
    return list(map(list, tuple_list))

class TestConvertToListOfLists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(convert_to_list_of_lists([]), [])

    def test_single_tuple(self):
        self.assertEqual(convert_to_list_of_lists([(1, 2)]), [[1, 2]])

    def test_multiple_tuples(self):
        self.assertEqual(convert_to_list_of_lists([(1, 2), (3, 4)]), [[1, 2], [3, 4]])

if __name__ == "__main__":
    unittest.main()
