# Write a Python program to sort a tuple by its float element.


import unittest

def tuple_optn(input_tuple):
    modified_tuple = int("".join(map(str,input_tuple)))
    return modified_tuple



class TestTuple(unittest.TestCase):

    def test_Tuple(self):
        original_Tuple = (10, 20, 40, 5, 70)
        expected = 102040570
        self.assertEqual(expected, tuple_optn(original_Tuple))



if __name__ == "__main__":
    unittest.main()


