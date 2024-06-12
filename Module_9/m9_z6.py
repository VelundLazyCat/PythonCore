import re

text = """The resulting profit was: 
    from the southern possessions $ 100, 
    from the northern colonies $500, 
    and the king gave $1000."""


def generator_numbers(string=""):

    numbers = re.findall('\d+', string)
    for num in numbers:
        yield num


def sum_profit(string):
    sum = 0
    for i in generator_numbers(string):
        sum = sum + int(i)
    return sum
