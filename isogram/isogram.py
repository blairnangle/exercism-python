import re


def is_isogram(string):
    letters = list(re.findall("[a-z]", string.lower()))

    return not any(freq > 1 for freq in [letters.count(letter) for letter in letters])
