# Simple and basic python Object oriented calculator with test and unittest - design pattern
## Strategy is a behavioral design pattern that turns a set of behaviors into objects and makes them interchangeable inside original context object.

Usage examples: The Strategy pattern is very common in Python code. It’s often used in various frameworks to provide users a way to change the behavior of a class without extending it.

Identification: Strategy pattern can be recognized by a method that lets a nested object do the actual work, as well as a setter that allows replacing that object with a different one.

## Run tests

Make sure you installed nose2

```bash
python -m nose2
```

Or basically run 

```bash
python test_ ...... .py files
```

## Usage

For simple-oop:

```python
calculator_object = Calculator()
calculator_object(5, 5, '+')
```

or 

```python
calculator_object = Calculator()
calculator_object.first_number = 5
calculator_object.second_number = 5
calculator_object.operation = '+'
calculator_object.calc()
```

for strategy-design-pattern:

```python
calculator_object = Calculator()
calculator_object.first_number = 5
calculator_object.second_number = 5
calculator_object.operation = Sum_strategy()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)