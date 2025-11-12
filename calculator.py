"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b / a # raise ZeroDivisionError if a == 0

def log(a, b):
    if a = 0:
        raise ValueError("No log base 0")
    return math.log(b, a)
    #loga(b) use math library + raise ValueError

def exp(a, b):
    return math.pow(a,b)

