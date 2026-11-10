"""
calculator.py
- Defines functions used to create a simple calculator
testing....
One function per operation, in order.
"""
import math
# First example
def square_root(a):
    if a < 0:
        raise ValueError('invalid input')
    return math.sqrt(a)

def hypotenuse(a, b):
    c = (a**2 + b**2)**0.5
    return c

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('no division by zero')
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError('invalid input')
    return math.log(b,a)

def exp(a, b):
    return a**b
