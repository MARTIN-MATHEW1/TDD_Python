from collections import ChainMap
import unittest


def create_family(Dict1, Dict2, Dict3):

    family = ChainMap(Dict1, Dict2)

    son = Dict3
    family = family.new_child(son)

    return family


class TestChainMap(unittest.TestCase):

    def test_chain_map(self):
        mom = {"name": "Jane", "age": 31}
        dad = {"name": "John", "age": 35}
        son = {"name": "Mike", "age": 0}

        
        family = create_family(mom, dad, son)
        
        
        # Check the contents of the ChainMap
        self.assertEqual(len(family.maps), 3)
        
        # Check values from the innermost dictionary
        self.assertEqual(family['name'], "Mike")
        self.assertEqual(family['age'], 0)
        
        # Check values from the middle dictionary
        self.assertEqual(family.maps[1]['name'], "Jane")
        self.assertEqual(family.maps[1]['age'], 31)
        
        # Check values from the outermost dictionary
        self.assertEqual(family.maps[2]['name'], "John")
        self.assertEqual(family.maps[2]['age'], 35)

if __name__ == "__main__":
    unittest.main()
