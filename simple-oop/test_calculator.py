from calculator import Calculator

def test_sum():
    calculator_object = Calculator()
    assert calculator_object.sum(5, 5) == 10, "Should be 10"

def test_sub():
    calculator_object = Calculator()
    assert calculator_object.sub(5, 5) == 0, "Should be 0"

def test_mul():
    calculator_object = Calculator()
    assert calculator_object.mul(5, 5) == 25, "Should be 25"

def test_div():
    calculator_object = Calculator()
    assert calculator_object.div(5, 5) == 1, "Should be 11"

def test_call_sum():
    calculator_object = Calculator()
    assert calculator_object(5, 5, '+') == 10, "Should be 10"

def test_call_sub():
    calculator_object = Calculator()
    assert calculator_object(5, 5, '-') == 0, "Should be 0"

def test_call_mul():
    calculator_object = Calculator()
    assert calculator_object(5, 5, '*') == 25, "Should be 25"

def test_call_div():
    calculator_object = Calculator()
    assert calculator_object(5, 5, '/') == 1, "Should be 11"

if __name__ == "__main__":

    test_sum()
    test_sub()
    test_mul()
    test_div()
    test_call_sum()
    test_call_sub()
    test_call_mul()
    test_call_div()

    print("Everything passed")
