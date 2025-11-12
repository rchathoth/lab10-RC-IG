import math


def square_root(a):
    try:
        math.sqrt(a)
    except:
        print("Error: Cannot square root a negative number!")

def hypotenuse(a, b): 
    math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError("Can't divide by 0!")
    return b / a

def log(a,b):
    if a == 0:
        raise ValueError("Logarithm cannot take 0 as an argument!")
    return math.log(b, a)

def exp(a,b):
    return a ** b

