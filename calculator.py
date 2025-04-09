# https://github.com/lu2400/lab10-OI-KH
# Partner 1: Lu Ighodalo
# Partner 2: Kian Hidalgo

import math

"""
calculator.py
- Defines functions used to create a simple calculatorr

One function per operation, in order.
"""
def square_root(a): 
    if a < 0:
        raise ValueError("ValueError")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

# First example

def add(a, b): 
    result = a + b
    return result

def mul(a, b):
    result = a * b
    return result

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    result = b/a
    return result

def exp(a, b):
    result = a ** b
    return result

def subtract(a, b): a - b

def logarithm(b, a):
    if a <= 0 or b <= 0:
        raise ValueError("ValueError")
    return math.log(b, a)
