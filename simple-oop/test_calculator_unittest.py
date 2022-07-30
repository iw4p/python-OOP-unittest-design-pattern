from calculator import Calculator
import unittest

class TestCalcs(unittest.TestCase):

    def test_sum(self):
        calculator_object = Calculator()
        self.assertEqual(calculator_object.sum(5,5), 10, "Should be 10")

    def test_sub(self):
        calculator_object = Calculator()
        self.assertEqual(calculator_object.sub(5,5), 0, "Should be 0")

    def test_mul(self):
        calculator_object = Calculator()
        self.assertEqual(calculator_object.mul(5,5), 25, "Should be 25")

    def test_div(self):
        calculator_object = Calculator()
        self.assertEqual(calculator_object.div(5,5), 1, "Should be 1")
    
if __name__ == '__main__':
    unittest.main()
