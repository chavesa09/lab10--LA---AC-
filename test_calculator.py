import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertTrue(add(1, -1) == 0)
        self.assertTrue(add(1, 10) == 11)
        self.assertFalse(add(1, 11) == 11)


    def test_subtract(self): # 3 assertions
        self.assertTrue(subtract(1, -1) == 2)
        self.assertTrue(subtract(1, 10) == -9)
        self.assertTrue(subtract(10, 0) == 10)
    # ######## Partner 1
    # def test_multiply(self): # 3 assertions
    # #     fill in code
    #
    # def test_divide(self): # 3 assertions
    # #     fill in code
    # # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(ZeroDivisionError)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(2, 8), 3)
        self.assertTrue(logarithm(100, 10) != 1)

    def test_log_invalid_base(self): # 1 assertion
       self.assertRaises(ValueError)

    # ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    # #     # call log function inside, example:
    # #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    # #     #     logarithm(0, 5)
    # #     fill in code
    #
    # def test_hypotenuse(self): # 3 assertions
    # #     fill in code
    #
    # def test_sqrt(self): # 3 assertions
    # #     # Test for invalid argument, example:
    # #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    # #     #    square_root(NUM)
    # #     # Test basic function
    # #     fill in code
    # ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()