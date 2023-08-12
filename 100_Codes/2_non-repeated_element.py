#  Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}


import unittest



class dict_test(unittest.TestCase):
    def test_make_dict(self):
        Original_list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
        expected_dict = {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}





if __name__ == "__main__":
    unittest.main

