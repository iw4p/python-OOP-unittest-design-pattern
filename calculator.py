class Calculator():
    def __init__(self):
        self._first_number = 0
        self._second_number = 0
        self._operation = ''

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
    def operation(self):
        return self._operation

    @first_number.setter
    def first_number(self, new_number):
        self._first_number = new_number

    @second_number.setter
    def second_number(self, new_number):
        self._second_number = new_number

    @operation.setter
    def operation(self, new_operation):
        self._operation = new_operation

    def sum(self, n1, n2):
        self._first_number = n1
        self._second_number = n2
        result_number = self._first_number + self._second_number
        return result_number

    def sub(self, n1, n2):
        self._first_number = n1
        self._second_number = n2
        result_number = self._first_number - self._second_number
        return result_number

    def mul(self, n1, n2):
        self._first_number = n1
        self._second_number = n2
        result_number = self._first_number * self._second_number
        return result_number

    def div(self, n1, n2):
        if n2 != 0:
            self._first_number = n1
            self._second_number = n2
            result_number = self._first_number / self._second_number
            return result_number
        else:
            raise ValueError("Sorry, no numbers below zero")
    
    def calc(self):
        if self._operation == '+':
            return (self.sum(self._first_number, self._second_number))
        elif self._operation == '*':
            return (self.mul(self._first_number, self._second_number))
        elif self._operation == '-':
            return (self.sub(self._first_number, self._second_number))
        elif self._operation == '/':
            return (self.div(self._first_number, self._second_number))


    def __call__(self, n1, n2, operation):
        if operation == '+':
            return (self.sum(self._first_number, self._second_number))
        elif operation == '*':
            return (self.mul(self._first_number, self._second_number))
        elif operation == '-':
            return (self.sub(self._first_number, self._second_number))
        elif operation == '/':
            return (self.div(self._first_number, self._second_number))
