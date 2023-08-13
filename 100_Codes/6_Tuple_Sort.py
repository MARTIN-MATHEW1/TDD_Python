# Write a Python program to sort a tuple by its float element.


import unittest

def tuple_optn(input_tuple):
    modified_tuple = (sorted(input_tuple, key = lambda x: float(x[1]), reverse= True))
    print(modified_tuple)
    return modified_tuple



class TestDictMaxMin(unittest.TestCase):

    def test_dict_max_min(self):
        orginal_tuple  = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
        new_tuple = [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')] 
        self.assertEqual(new_tuple, tuple_optn(orginal_tuple))


if __name__ == "__main__":
    unittest.main()


