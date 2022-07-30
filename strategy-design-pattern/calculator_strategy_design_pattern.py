from math import factorial
from abc import ABC, abstractmethod
from typing import List

class Operation_strategy(ABC):
    @abstractmethod
    def do_operation(self, n1, n2):
        pass

class Sum_strategy(Operation_strategy):
    def do_operation(self, n1, n2):
        return n1 + n2

class Sub_strategy(Operation_strategy):
    def do_operation(self, n1, n2):
        return n1 - n2

class Mul_strategy(Operation_strategy):
    def do_operation(self, n1, n2):
        return n1 * n2

class Div_strategy(Operation_strategy):
    def do_operation(self, n1, n2):
        if n2 != 0:
            result_number = n1 / n2
            return result_number
        else:
            raise ValueError("Sorry, no numbers below zero")

class Calculator():
    def __init__(self):
        self._first_number = 0
        self._second_number = 0
        self._operation = None

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

    @property
    def operation(self) -> Operation_strategy:
        return self._operation

    @operation.setter
    def operation(self, operation: Operation_strategy) -> None:
        self._operation = operation

    @first_number.setter
    def first_number(self, new_number):
        self._first_number = new_number

    @second_number.setter
    def second_number(self, new_number):
        self._second_number = new_number

    def __call__(self):
        return (self._operation.do_operation(self.first_number, self.second_number))