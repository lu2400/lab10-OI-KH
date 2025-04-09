import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
<<<<<<< HEAD
def square_root(a): 
    if a < 0:
        raise ValueError("ValueError")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)
=======
import math

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
    result = b / a
    return result

def exp(a, b):
    result = a ** b
    return result
>>>>>>> ecb1ba6bd68a47ca9658d16a1515106647435b2b

def subtract(a, b): a - b

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("ValueError")
    return math.log(a, b)
