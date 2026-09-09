import math


def some_expression_with_rounding(a, b):
    denominator = 1 + a ** (2 ** b)
    result = (12 * a + 25 * b) / denominator
    return math.ceil(result * 100) / 100
