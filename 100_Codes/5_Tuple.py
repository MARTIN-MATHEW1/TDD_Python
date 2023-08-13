# Write a Python program to remove an empty tuple(s) from a list of tuples.
# Write a Python program to replace the last value of tuples in a list.


import unittest

def tuple_optn(input_tuple):
    modified_tuple = [ i[:-1]+(100,) for i in input_tuple]
    return modified_tuple

def tuple_optn_2(input_tuple):
    modified_tuple = [i for i in input_tuple if i]
    return modified_tuple


class TestDictMaxMin(unittest.TestCase):

    def test_dict_max_min(self):
        orginal_tuple  =  [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
        new_tuple = [(10, 20, 100), (40, 50, 100), (70, 80, 100)] 
        self.assertEqual(new_tuple, tuple_optn(orginal_tuple))

        empty_tuples = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
        non_empty_tuples = [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']  
        self.assertEqual(non_empty_tuples, tuple_optn_2(empty_tuples))


if __name__ == "__main__":
    unittest.main()

