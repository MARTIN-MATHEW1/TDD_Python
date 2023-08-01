import unittest
import Discount_Calculator


class Discount_calculator(unittest.TestCase):
    def test_Discount_calculator(self):
        Final_Price = Discount_Calculator.Item(150,50,10)
        print(Final_Price)
        # Final_Price = Final_Price.apply_discount()
        Discounted_Price = 750
        self.assertEqual(Final_Price, Discounted_Price)



if __name__ == "__main__":
    unittest.main()