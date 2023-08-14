

import unittest


def set_remover(sn1,sn2):
    print(~(sn1.intersection(sn2)), "hi")
    for i in sn1&sn2:
        sn1.remove(i)
        sn2.remove(i)
    print(sn1.intersection(sn2), "hi")
    return sn1.union(sn2)


class TestFindMissingNumbers(unittest.TestCase):

    def test_missing_in_set1(self):
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
   
        self.assertEqual(set_remover(set1, set2), {1,2,5,6})

    # def test_missing_in_set2(self):
    #     set1 = {1, 2, 3, 4}
    #     set2 = {3, 4, 5, 6}
    #     _, missing_set2 = find_missing_numbers(set1, set2)
    #     self.assertEqual(missing_set2, {1, 2})

    # def test_no_missing_numbers(self):
    #     set1 = {1, 2, 3}
    #     set2 = {1, 2, 3}
    #     missing_set1, missing_set2 = find_missing_numbers(set1, set2)
    #     self.assertEqual(missing_set1, set())
    #     self.assertEqual(missing_set2, set())

if __name__ == "__main__":
    unittest.main()
