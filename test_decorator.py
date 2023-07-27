import unittest
import Decorator_use

class Decorator_Test(unittest.TestCase):
    def test_sorted_names_with_age(self):
        expected = [ "Mrs.Alice Ben","Mr.Martin Mathew","Mr.James Dani"]
        input_name_and_details = [["James","Dani", "M", 30], 
                                  ["Martin","Mathew", "M", 25], 
                                  ["Alice","Ben", "F", 18]]
        Result = Decorator_use.Name_and_Details(input_name_and_details)
        self.assertEqual(expected, Result)

if __name__ == "__main__":
    unittest.main()