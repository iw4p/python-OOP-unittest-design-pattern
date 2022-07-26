from calculator import Calculator
import unittest

class TestCalcs(unittest.TestCase):

    def test_sum(self):
        calculator_object = Calculator()
        self.assertEqual(calculator_object.sum(5,5) == 10, True)

    def test_sub(self):
        calculator_object = Calculator()
        self.assertEqual(calculator_object.sub() == 0, "Should be 0")

    def test_mul(self):
        calculator_object = Calculator()
        self.assertEqual(calculator_object.mul() == 25, "Should be 25")

    def test_div(self):
        calculator_object = Calculator()
        self.assertEqual(calculator_object.div() == 1, "Should be 11")
    
if __name__ == '__main__':
    unittest.main()
