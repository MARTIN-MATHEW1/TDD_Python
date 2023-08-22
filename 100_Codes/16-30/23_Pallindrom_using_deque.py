from collections import deque
import unittest

def is_palindrome(input_str):

    filtered_str = ''.join(filter(str.isalnum, input_str.lower()))
    dqued_str = deque(filtered_str)
    
    # print(dqued_str)
    while len(dqued_str) > 1:
        if dqued_str.popleft() != dqued_str.pop():
            return False

    return True



class TestPalindrome(unittest.TestCase):

    def test_pallindrome(self):
        input_str_1 = "Pappi"
        input_str_2 = "A man2, a plan, a canal, Pa2nama!"


        self.assertFalse(is_palindrome(input_str_1))  
        self.assertTrue(is_palindrome(input_str_2))  

       

        


if __name__ == "__main__":
    unittest.main()







