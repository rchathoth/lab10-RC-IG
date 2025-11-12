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

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #
        self.assertRaises(div(0,5), ZeroDivisionError)
    #    

    def test_logarithm(self): # 3 assertions
        self.assertRaises(log(0, 3), ValueError)

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()