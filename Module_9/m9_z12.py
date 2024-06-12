from functools import reduce
payment = [1, -3, 4]

def amount_payment(payment):
    new=[]
    for i in payment:
        if i>0:
            new.append(i)
    return reduce(lambda x, y: x+y, new)



def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum