# https://github.com/rchathoth/lab10-RC-IG.git
# Partner 1: Ishmael Goodridge
# Partner 2: Rohit Chathoth


import math

def square_root(a):
    if a < 0:
        raise ValueError('a must be non-negative')
    return math.sqrt(a)# raise ValueError if a < 0

def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('division by zero')
    return b / a

def logarithm(a, b):
    if a == 0:
        raise ValueError("No log base 0")
    if b <=0:
        raise ValueError("No negative base")
    return math.log(b, a)
    #loga(b) use math library + raise ValueError

def exp(a, b):
    return math.pow(a,b)

