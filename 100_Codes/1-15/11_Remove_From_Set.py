# Write a Python program to remove an item from a set if it is present in the set. 

import unittest

def remove_item_from_set(input_set, item):
    input_set.discard(item)

class TestRemoveItemFromSet(unittest.TestCase):

    def test_remove_existing_item(self):
        input_set = {1, 2, 3, 4}
        item_to_rmv = 3
        remove_item_from_set(input_set, item_to_rmv)
        self.assertNotIn(item_to_rmv, input_set)

    def test_remove_nonexisting_item(self):
        input_set = {1, 2, 3, 4, 5}
        item_to_rmv = 5
        remove_item_from_set(input_set, item_to_rmv)
        self.assertNotIn(item_to_rmv, input_set)

if __name__ == "__main__":
    unittest.main()
