from calculator import Calculator

def test_sum():
    assert calculator_object.sum(5, 5) == 10, "Should be 10"

def test_sub():
    assert calculator_object.sub(5, 5) == 0, "Should be 0"

def test_mul():
    assert calculator_object.mul(5, 5) == 25, "Should be 25"

def test_div():
    assert calculator_object.div(5, 5) == 1, "Should be 11"

if __name__ == "__main__":

    calculator_object = Calculator()
    # calculator_object.first_number = 5
    # calculator_object.second_number = 5

    test_sum()
    test_sub()
    test_mul()
    test_div()

    print("Everything passed")
