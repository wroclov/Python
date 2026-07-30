
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Provided arguments are not allowed for division, only int, float or Decimal accepted")
    if not isinstance(a, (int, float, Decimal)) or not isinstance(b,(int, float, Decimal)):
        raise TypeError("Provided arguments are not allowed for division, only int, float or Decimal accepted")
    if b == 0:
        raise ValueError("Division by zero is undefined")
    return Decimal(a) / Decimal(b)

def power(base, exponent):
    return base ** exponent
