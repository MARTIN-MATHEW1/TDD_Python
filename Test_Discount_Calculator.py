import unittest
import Discount_Calculator


class Discount_calculator(unittest.TestCase):
    def test_Discount_calculator(self):
        Final_Price = Discount_Calculator.Item(150,50,10)
        output_Str = "The orginal price was 1500 you got it for 750.0"
        self.assertEqual(output_Str,str(Final_Price) )


if __name__ == "__main__":
    unittest.main()