import re


def is_shouting(hey_bob):
    return re.sub(r"\W+", "", hey_bob).isupper()


def is_question(hey_bob):
    return hey_bob[-1:] == "?"


def response(hey_bob):
    stripped = "".join(hey_bob.split())
    print(stripped)
    if is_shouting(stripped) and is_question(stripped):
        return "Calm down, I know what I'm doing!"
    if is_question(stripped):
        return "Sure."
    if is_shouting(stripped):
        return "Whoa, chill out!"
    if "" == stripped:
        return "Fine. Be that way!"

    return "Whatever."
