import math
from typing import Generator


def calculate_upper_limit(n: int) -> [int]:
    return math.ceil(n * math.log(n * math.log(n))) + 1


def prime_generator(limit: int) -> Generator[int, None, None]:
    mask: [bool] = [True] * limit
    for i in range(2, limit):
        if mask[i]:
            yield i
            for c in range(i * i, limit, i):
                mask[c] = False


def prime(n) -> int:
    match n:
        case 0:
            raise ValueError("there is no zeroth prime")
        case 1:
            return 2
        case 2:
            return 3
        case 3:
            return 5
        case _:
            generator: Generator[int, None, None] = prime_generator(
                calculate_upper_limit(n)
            )

            return next(x for i, x in enumerate(generator) if i == n - 1)
