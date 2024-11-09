from decimal import Decimal
'''
The Decimal type in Python is part of the decimal module and provides a way to represent and perform 
arithmetic on decimal floating-point numbers with high precision. 
It is especially useful when you need to avoid issues like rounding errors 
that can occur with binary floating-point numbers (float type) in situations requiring exact decimal representation
 (e.g., financial calculations, scientific measurements).
'''

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if type(a) not in (int, float, Decimal) or type(b)not in (int, float, Decimal):
        raise TypeError("Provided arguments are not allowed for division, only int, float or Decimal accepted")
    if b == 0:
        raise ValueError("Division by zero is undefined")
    return Decimal(a) / Decimal(b)

def power(base, exponent):
    return base ** exponent
