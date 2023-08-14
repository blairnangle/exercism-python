import re

VOWELS = {"a", "e", "i", "o", "u"}


def match_leading_consonant_and_qu_sound(word):
    return re.match("([^aeiou]*qu)", word)


def get_leading_consonant_and_qu_sound(word):
    return str(match_leading_consonant_and_qu_sound(word).group(1))


def match_leading_consonant_and_y_sound(word):
    return re.match("([^aeiou]+y)", word)


def get_leading_consonant_sound_before_y(word):
    return str(re.match("([^aeiou]+)y", word).group(1))


def get_leading_consonant_sound(word):
    return str(re.match("([^aeiou]*)", word).group(1))


def translate_word(word):
    if word[:1] in VOWELS:
        return word + "ay"
    if word[:2] in {"xr", "yt"}:
        return word + "ay"
    if match_leading_consonant_and_qu_sound(word):
        leading_consonant_and_qu_sound = get_leading_consonant_and_qu_sound(word)
        return (
            word[len(leading_consonant_and_qu_sound) :]
            + leading_consonant_and_qu_sound
            + "ay"
        )
    if match_leading_consonant_and_y_sound(word):
        leading_consonant_sound = get_leading_consonant_sound_before_y(word)
        return word[len(leading_consonant_sound) :] + leading_consonant_sound + "ay"
    else:
        leading_consonant_sound = get_leading_consonant_sound(word)
        return word[len(leading_consonant_sound) :] + leading_consonant_sound + "ay"


def translate(text):
    return " ".join(map(lambda word: translate_word(word), text.split(" ")))
