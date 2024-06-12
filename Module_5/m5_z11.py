import re


def find_all_words(text, word):
    numbers = []

    numbers = re.findall(word, text, re.IGNORECASE)
    return numbers
