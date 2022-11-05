"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return f"un{word}"


def add_prefix(prefix, word):
    return f"{prefix}{word}"


def add_suffix(word, suffix):
    return f"{word}{suffix}"


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    prefix = vocab_words[0]

    return " :: ".join([prefix] + [add_prefix(prefix, word) for word in vocab_words[1:]])


def replace_last_letter(word, new_letter):
    return word[0:len(word) - 1] + new_letter


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    length_of_word = len(word)
    word_without_suffix = word[0:length_of_word - 4]
    if word_without_suffix[len(word_without_suffix) - 1] == "i":
        return replace_last_letter(word_without_suffix, "y")
    else:
        return word_without_suffix


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """

    return add_suffix(sentence.split()[index].replace(".", ""), "en")
