#  Write a Python program to merge more than one dictionary into a single expression. 

import collections as ct
import unittest

def merge_dict(*args):
    merged_dict = dict(ct.ChainMap({}, *args))
    print("here", ct.ChainMap({}, *args))
    return merged_dict


class Colors(unittest.TestCase):
    def test_merged(self):

        c_1 = { "R": "Red", "B": "Black", "P": "Pink" }
        c_2 = { "G": "Green", "W": "White" }
        color1 = { "R": "Red", "B": "Black", "P": "Pink" }
        color2 = { "G": "Green", "W": "White" }
        color3 = { "O": "Orange", "W": "White", "B": "Black" }
        expected = {'G': 'Green', 'W': 'White', 'R': 'Red', 'B': 'Black', 'P': 'Pink'}

        self.assertEqual(expected, merge_dict(c_1, c_2))


        # print(merge_dict(color1,color2, color3))

if __name__=="__main__":
    unittest.main()


