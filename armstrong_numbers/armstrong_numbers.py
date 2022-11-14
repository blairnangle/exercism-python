from functools import reduce


def is_armstrong_number(n):
    n_str = str(n)
    n_len = len(n_str)

    return reduce(lambda x, y: x + y, map(lambda digit: int(digit) ** n_len, list(n_str))) == n
