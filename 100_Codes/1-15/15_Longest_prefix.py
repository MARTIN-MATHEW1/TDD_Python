# Write a Python program to find the longest common prefix of all strings. Use the Python set. 

import unittest

def longest_common_prefix(strings):
    if not strings:
        return ""

    shortest_string = min(strings, key=len)
    for i, char in enumerate(shortest_string):
        if any(s[i] != char for s in strings):
            return shortest_string[:i]
    return shortest_string

class TestLongestCommonPrefix(unittest.TestCase):

    def test_common_prefix(self):
        string_list = ["flower", "flow", "flight"]
        common_prefix = longest_common_prefix(string_list)
        self.assertEqual(common_prefix, "fl")

    def test_empty_list(self):
        string_list = []
        common_prefix = longest_common_prefix(string_list)
        self.assertEqual(common_prefix, "")

    def test_no_common_prefix(self):
        string_list = ["apple", "banana"]
        common_prefix = longest_common_prefix(string_list)
        self.assertEqual(common_prefix, "")

if __name__ == "__main__":
    unittest.main()
