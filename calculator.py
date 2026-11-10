"""
calculator.py
- Defines functions used to create a simple calculator
testing....
One function per operation, in order.
"""
import math
# First example
def square_root(a):
    math.sqrt(a)
    if a < 0:
        raise ValueError('invalid input')

def hypotenuse(a, b):
    math.hypot(a, b)


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError('division by zero')
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError('invalid input')
    return math.log(b,a)

def exponent(a, b):
    return a**b

print('hello world')

print(exponent(2,3))
