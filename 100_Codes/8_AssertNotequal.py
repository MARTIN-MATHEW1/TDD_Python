import unittest

def remove_duplicates(lst):

    return list(map(lambda x: x, set(lst)))

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        orig_lst = [1, 2, 2, 3, 4, 4, 5, 6, 6]
        result = remove_duplicates(orig_lst)

        self.assertNotEqual(orig_lst, result)

if __name__ == "__main__":
    unittest.main()
