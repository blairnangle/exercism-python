"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time: int):
    """
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers: int):
    """
    :param layers: int - number of layers the lasagne will be
    :return: int - preparation time based on the number of layers
    """

    return layers * 2


def elapsed_time_in_minutes(layers: int, elapsed_bake_time: int):
    """
    :param layers: int - number of layers the lasagne will be
    :param elapsed_bake_time: int - duration in minutes the lasagne has already spent baking
    :return: int - total time spent creating lasagne so far
    """

    return preparation_time_in_minutes(layers) + elapsed_bake_time
