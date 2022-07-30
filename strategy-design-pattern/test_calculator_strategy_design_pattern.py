from calculator_strategy_design_pattern import *

def test_sum():
    calculator_object = Calculator()

    calculator_object.first_number = 5
    calculator_object.second_number = 5
    
    calculator_object.operation = Sum_strategy()
    
    assert calculator_object() == 10, "Should be 10"

def test_sub():
    calculator_object = Calculator()

    calculator_object.first_number = 5
    calculator_object.second_number = 5
    
    calculator_object.operation = Sub_strategy()

    assert calculator_object() == 0, "Should be 0"

def test_mul():
    calculator_object = Calculator()

    calculator_object.first_number = 5
    calculator_object.second_number = 5
    
    calculator_object.operation = Mul_strategy()
    assert calculator_object() == 25, "Should be 25"

def test_div():
    calculator_object = Calculator()

    calculator_object.first_number = 5
    calculator_object.second_number = 5
    
    calculator_object.operation = Div_strategy()
    assert calculator_object() == 1, "Should be 11"

if __name__ == "__main__":

    test_sum()
    test_sub()
    test_mul()
    test_div()

    print("Everything passed")
