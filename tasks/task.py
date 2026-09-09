import math

def calculate(a, b):
    result = (12 * a + 25 * b) / (1 + a**(2**b))
    return math.ceil(result * 100) / 100
