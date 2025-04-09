import math

"""
calculator.py
- Defines functions used to create a simple calculatorr

One function per operation, in order.
"""
import math

# First example

def add(a, b): 
    result = a + b
    return result
def sub(a, b):
    result = a - b
    return result
def mul(a, b):
    result = a * b
    return result
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    result = b/a
    return result

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    result = math.log(a, b)
    return result

def exp(a, b):
    result = a ** b
    return result

def add(a, b): a + b


def multiply(a, b): a * b

def divide(a, b):
    if a == 0:
        raise ValueError("ZeroDivisionError")
    return a / b

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("ValueError")
    return math.log(a, b)

def exponent(a, b):
    if a < 0 and b != int(b):
        raise ValueError("ValueError")
    return a ** b   
