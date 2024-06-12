import re

text1 = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
word1 = "Python"
exampl = {'result': True,
          'first_index': 34,
          'last_index': 40,
          'search_string': '',
          'string': ''}
exampl2 = {
    'result': False,
    'first_index': None,
    'last_index': None,
    'search_string': '',
    'string': ''}


def find_word(text, word):
    examp = {'result': None,
             'first_index': None,
             'last_index': None,
             'search_string': None,
             'string': None}
    result = re.search(word, text)
    if result:
        examp['result'] = True
        examp['first_index'] = result.span()[0]
        examp['last_index'] = result.span()[1]
        examp['search_string'] = result.group()
        examp['string'] = text
    else:
        examp['result'] = False
        examp['first_index'] = None
        examp['last_index'] = None
        examp['search_string'] = word
        examp['string'] = text
    return examp


print(find_word(text1, word1))
