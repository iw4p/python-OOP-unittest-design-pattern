from math import factorial

class Calculator():
    def __init__(self):
        self._first_number = 0
        self._second_number = 0
        self._result = 0

    def __str__(self):
        return f'{self._first_number}, {self._second_number}'
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self._first_number}, {self._second_number})'
    
    @property
    def first_number(self):
        return self._first_number

    @property
    def second_number(self):
        return self._second_number

    @first_number.setter
    def first_number(self, new_number):
        self._first_number = new_number

    @second_number.setter
    def second_number(self, new_number):
        self._second_number = new_number

    def sum(self, n1, n2):
        result_number = n1 + n2
        return result_number

    def sub(self, n1, n2):
        result_number = n1 - n2
        return result_number

    def mul(self, n1, n2):
        result_number = n1 * n2
        return result_number

    def div(self, n1, n2):
        if n2 != 0:
            result_number = n1 / n2
        else:
            raise ValueError("Sorry, no numbers below zero")
        return result_number

    def __call__(self, n1, n2, operation):
        if operation == '+':
            print(self.sum(n1, n2))
        elif operation == '*':
            print(self.mul(n1, n2))
        elif operation == '-':
            print(self.sub(n1, n2))
        elif operation == '/':
            print(self.div(n1, n2))

c1 = Calculator()