from decimal import Decimal, getcontext

list1 = [3, 5, 77, 23, 0.57]
list2 = [31, 55, 177, 2300, 1.57]
count1 = 6
count2 = 9
otvet1 = 21.714
otvet2 = 512.91400


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    a = 0
    Decimal(a)
    for i in number_list:
        a += Decimal(i)
    return a/Decimal(len(number_list))


print(decimal_average(list1, count1))
print(decimal_average(list2, count2))
