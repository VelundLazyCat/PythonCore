import re

text1 = 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn '
spam_words1 = ['began', 'Python']


def is_spam_words(text, spam_words):

    for sp in spam_words:

        text = re.sub(sp, '*'*len(sp), text, flags=re.IGNORECASE)

    return text


print(is_spam_words(text1, spam_words1))
