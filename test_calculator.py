import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2

    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-3, 2), -1)


    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5,4), 1)
        self.assertEqual(sub(4, 5), -1)
        self.assertEqual(sub(0,0), 0)
        self.assertEqual(sub(-4, -5), 1)
        self.assertEqual(sub(4, -2), 6)
        self.assertEqual(sub(0,-2), 2)
        self.assertEqual(sub(-3,0), -3)


    # Partner 1
    def test_multiply(self): # 3 assertions
        pass

    def test_divide(self): # 3 assertions
        pass
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(8, 2), 3)
        self.assertEqual(log(1, 10), 0)
        self.assertEqual(log(2, 0.5), -1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            log(10, 1)

    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        pass

    def test_hypotenuse(self): # 3 assertions
        pass

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        pass
    ##########################

# Do not touch thiss
if __name__ == "__main__":
    unittest.main()