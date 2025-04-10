"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example

import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a # raise ZeroDivisionError if a == 0

def log(a, b):
    if b <= 0:
        raise ValueError
    if a <= 0 or a == 1
        raise ValueError
    return math.log(b, a)# use math library + raise ValueError

def exp(a, b):
    return ab

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def logarithm(a, b):
    if b <= 0:
        raise ValueError("Logarithm undefined: b must be positive.")
        # Check that the base a is positive and not equal to 1
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base a must be positive and not equal to 1.")
    return math.log(b, a)

def exponent(a, b):
    return a**b




