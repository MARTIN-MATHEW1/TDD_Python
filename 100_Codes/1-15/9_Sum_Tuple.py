# Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.


import unittest

def sum_of_tuples_elements(tuple_list):

    # return [sum(x) for x in tuple_list]
    result =  map(sum, tuple_list)
    # print("hi",list(result))
    return (list(result))

class TestSumOfTuplesElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_of_tuples_elements([]), [])

    def test_single_tuple(self):
        self.assertEqual(sum_of_tuples_elements([(1, 2, 3)]), [6])

    def test_multiple_tuples(self):
        self.assertEqual(sum_of_tuples_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)]), [6, 15, 24])

if __name__ == "__main__":
    unittest.main()
