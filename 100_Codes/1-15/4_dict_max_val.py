#  Write a Python program to find the key of the maximum value in a dictionary. 

import unittest

def dict_max_min(inp_dict):
    return max(inp_dict, key = inp_dict.get), min(inp_dict, key = inp_dict.get)



class TestDictMaxMin(unittest.TestCase):

    def test_dict_max_min(self):
        orginal_dict  = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
        max_and_min = ('Roxanne', 'Theodore')
        self.assertEqual(max_and_min, dict_max_min(orginal_dict))



if __name__ == "__main__":
    unittest.main()
