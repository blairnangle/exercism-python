import math


def calculate_upper_limit(n: int) -> [int]:
    return math.ceil(n * math.log(n * math.log(n))) + 1


def prime_generator(n: int) -> [int]:
    limit = n + 3 if n <= 3 else calculate_upper_limit(n)
    mask: [bool] = [False, False] + [True] * limit
    primes: [int] = []
    for i in range(2, limit):
        if mask[i]:
            primes.append(i)
            for c in range(i * i, limit, i):
                mask[c] = False

    return primes


def prime(n) -> int:
    if n == 0:
        raise ValueError("there is no zeroth prime")
    else:
        primes: [int] = prime_generator(n)

        return primes[n - 1]
