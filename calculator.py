import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
def square_root(a): 
    if a < 0:
        raise ValueError("ValueError")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): a + b

def subtract(a, b): a - b    

def multiply(a, b): a * b

def divide(a, b):
    if a == 0:
        raise ValueError("ZeroDivisionError")
    return b / a 

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("ValueError")
    return math.log(a, b)

def exponent(a, b):
    if a < 0 and b != int(b):
        raise ValueError("ValueError")
    return a ** b   
