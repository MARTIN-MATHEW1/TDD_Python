# Write a Python program to find the item with the highest frequency in a given list.
#use defaultdict

from collections import defaultdict
import unittest


def send_most_occured(nums):
    dict_new = defaultdict(int)
    for i in nums:
        dict_new[i] +=1

    # oneliner to find return the key with max occured value !!
    return(list(dict_new.keys())[list(dict_new.values()).index(max(dict_new.values()))])
# print(dict_new)


class Test_most_ocurred(unittest.TestCase):
    # def test_num_most_ocurred(self):
    #     num_list= [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,23,3,3,3,3,3]
    #     self.assertEqual(send_most_occured(num_list), 3)
    def test_num_most_ocurred(self):
        num_list= []
        with self.assertRaises(ValueError) as context:
            send_most_occured([])
            print(context.exception)
        self.assertEqual(str(context.exception), "max() arg is an empty sequence")


if __name__ == "__main__":

    unittest.main()