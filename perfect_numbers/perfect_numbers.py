from functools import reduce


def find_factors(number):
    return [n for n in range(1, number // 2 + 1) if number % n == 0 and n != number]


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot = reduce(lambda x, y: x + y, find_factors(number), 0)

    if aliquot == number:
        return "perfect"
    if aliquot > number:
        return "abundant"

    return "deficient"
