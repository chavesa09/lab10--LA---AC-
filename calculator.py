# https://github.com/chavesa09/lab10--LA---AC-.git
# Partner 1: Luisa Almeida
# Partner 2: Alejandro Chaves

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError ("Cannot take the square root of zero")
    return math.sqrt(a)

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        raise

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a # raise ZeroDivisionError if a == 0

def exp(a, b):
    return a**b

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if b <= 0:
        raise ValueError("Logarithm undefined: b must be positive.")
        # Check that the base a is positive and not equal to 1
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base a must be positive and not equal to 1.")
    return math.log(b, a)




