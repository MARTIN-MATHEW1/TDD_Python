# Write a Python function to reverse a list at a specific location.

import unittest


def rev_on_input_pos(inp_list,start_pos,end_pos):

    sliced_list = inp_list[start_pos:end_pos]
    static_list = [x for x in inp_list if x not in sliced_list]
    rev_1 = list(reversed(sliced_list))
    static_list.extend(rev_1)

    return static_list


class test_list(unittest.TestCase):

    def test_rev(self):
        org_list = ["1","2","3","4","5","6","7"]
        reversed_at_2_and_7 =  ["1","2","7","6","5","4","3"]
        start_pos,end_pos = (2,7)
        print(rev_on_input_pos(org_list,start_pos,end_pos))
        self.assertEqual (reversed_at_2_and_7, rev_on_input_pos(org_list,start_pos,end_pos))

if __name__ == "__main__":
    unittest.main()
    
