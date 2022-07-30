from calculator_strategy_design_pattern import *
import unittest

class TestCalcs(unittest.TestCase):

    def test_sum(self):
        calculator_object = Calculator()
        calculator_object.first_number = 5
        calculator_object.second_number = 5
        calculator_object.operation = Sum_strategy()
        self.assertEqual(calculator_object(), 10, "Should be 10")

    def test_sub(self):
        calculator_object = Calculator()
        calculator_object.first_number = 5
        calculator_object.second_number = 5
        calculator_object.operation = Sub_strategy()
        self.assertEqual(calculator_object(), 0, "Should be 0")

    def test_mul(self):
        calculator_object = Calculator()
        calculator_object.first_number = 5
        calculator_object.second_number = 5
        calculator_object.operation = Mul_strategy()
        self.assertEqual(calculator_object(), 25, "Should be 25")

    def test_div(self):
        calculator_object = Calculator()
        calculator_object.first_number = 5
        calculator_object.second_number = 5
        calculator_object.operation = Div_strategy()
        self.assertEqual(calculator_object(), 1, "Should be 1")
    
if __name__ == '__main__':
    unittest.main()
