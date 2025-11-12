import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self): # 3 assertions
         self.assertEqual(add(1, 2), 3)
         self.assertEqual(add(1, 1000), 1001)
         self.assertEqual(add(-1, 2), 1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(1, 2), -1)
        self.assertEqual(sub(100, 2), 98)
        self.assertEqual(sub(0, 2), -2)
    # ##########################
    """
    https://github.com/rchathoth/lab10-RC-IG.git
    # Partner 1: Ishmael Goodridge
    # Partner 2: Rohit Chathoth
    """
    ######## Partner 1
    def test_multiply(self):
        a = 10
        b = 5
        if mul(a,b) != 50:
            print("mul function failure")

        a = 2
        b = 0
        if mul(a,b) != 0:
            print("mul function failure")

        a = 3
        b = -1
        if mul(a,b) != -3:
            print("mul function failure")

    def test_divide(self): # 3 assertions
        a = 5
        b = 10
        if div(a,b) != 2:
            print("div function failure")

        self.assertRaises(ZeroDivisionError, div, 10, 0)

        a = -3
        b = 30
        if div(a,b) != -10:
            print("div function failure")
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(ZeroDivisionError, div, 0, 5)
    #    

    def test_logarithm(self): # 3 assertions
        self.assertRaises(ValueError, log, 0, 3)

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        self.assertRaises(ValueError, log, 0, 5)# 1 assertion


    def test_hypotenuse(self): # 3 assertions
        a = 3
        b = 4
        if hypotenuse(a,b) != 5:
            print("hypotenuse function failure")

        a = 6
        b = 8
        if hypotenuse(a,b) != 10:
            print("hypotenuse function failure")

        a = 9
        b = 12
        if hypotenuse(a,b) != 15:
            print("hypotenuse function failure")

    def test_sqrt(self): # 3 assertions
        a = 4
        if square_root(a) != 2:
            print("sqrt function failure")

        self.assertRaises(ValueError, square_root, -4)

        a = 16
        if square_root(a) != 4:
            print("sqrt function failure")

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()