# https://github.com/chavesa09/lab10--LA---AC-.git
# Partner 1: Luisa Almeida
# Partner 2: Alejandro Chaves


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
    ####### Partner 1
    def test_multiply(self): # 3 assertions
        a = 1
        b= 0
        self.assertTrue(mul(a, b,) == 0)
        self.assertTrue(mul(-1, 5) == -5)
        self.assertTrue(mul(3, 3) == 9)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(3, 2 ) , 0.6666666)
        self.assertTrue(div(9, 1) == 9)
        self.assertTrue(div(-10, -10) == 1)
        self.assertTrue(div(-3, 3) == -1)

    ##########################

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
    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 5)  # base 0 is invalid
        with self.assertRaises(ValueError):
            logarithm(1, 5)  # base 1 is invalid
        with self.assertRaises(ValueError):
            logarithm(-2, 5)  # negative base is invalid

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse(-3, 4), 5.0)
        self.assertEqual(hypotenuse(0, 0), 0.0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(16), 4.0)
        self.assertEqual(square_root(0), 0.0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()