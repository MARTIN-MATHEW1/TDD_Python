import unittest
from collections import Counter

def max_least_char(str1):
    temp = Counter(str1) 
    max_char = max(temp, key=temp.get)
    min_char = min(temp, key=temp.get)
    return (max_char, min_char)

class TestMaxLeastChar(unittest.TestCase):

    def test_max_least_char(self):
        str1 = "hello world"
        result = max_least_char(str1)
        self.assertEqual(result, ('l', 'h'))

if __name__ == "__main__":
    unittest.main()