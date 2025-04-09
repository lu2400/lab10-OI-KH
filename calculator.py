# https://github.com/lu2400/lab10-OI-KH
# Partner 1: Lu Ighodalo
# Partner 2: Kian Hidalgo

import math

"""
calculator.py
- Defines functions used to create a simple calculatorr

One function per operation, in order.
"""
import math

# First example

def subtract(a, b):
    result = a - b
    return result

def mul(a, b):
    result = a * b
    return result

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    result = a/b
    return result

def square_root(a):
    if a < 0:
        raise ValueError("ValueError")
    result = math.sqrt(a)
    return result

def hypotenuse(a, b):
    return math.hypot(a, b)

def exp(a, b):
    if a < 0:
        raise ValueError("ValueError")
    result = a ** b
    return result

def add(a, b):
    return a + b

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("ValueError")
    return math.log(a, b)

