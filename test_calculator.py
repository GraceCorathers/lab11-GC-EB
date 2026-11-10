import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(5, 6), 11)
        self.assertEqual(add(4, 4), 8)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(7, 4), 3)
        self.assertEqual(subtract(10, 6), 4)
        self.assertEqual(subtract(4, 4), 0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 8), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(4, 20), 5)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 10)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaies(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(10, 100), 2)
        self.assertAlmostEqual(log(2, 16), 4)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10)


    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
         # call log function inside, example:
         # with self.assertRaises(<INSERT_ERROR_TYPE>):
         #     logarithm(0, 5)
         with self.assertRaises(ValueError):
             logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self): # 3 assertions
         # Test for invalid argument, example:
         # with self.assertRaises(<INSERT_ERROR_TYPE>):
         #    square_root(NUM)
         # Test basic function
         with self.assertRaises(ValueError):
             square_root(-4)
         self.assertAlmostEqual(square_root(9), 3)
         self.assertAlmostEqual(square_root(16), 4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()