from math import sqrt


def score(x, y):
    distance_from_center = sqrt(x**2 + y**2)
    if 0 <= distance_from_center <= 1:
        return 10
    elif 1 < distance_from_center <= 5:
        return 5
    elif 5 < distance_from_center <= 10:
        return 1

    return 0
