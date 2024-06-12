from random import randrange
import random

min = 1
max = 49
quantity = 6


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min > quantity or quantity > max:
        return []
    numbers_list = []
    for i in range(quantity):
        numbers_list.append(random.randint(min, max))
    numbers_list.sort()
    return numbers_list


print(get_numbers_ticket(min, max, quantity))
