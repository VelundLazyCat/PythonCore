def positive_values(list_payment):
    new_list = []
    for i in filter(lambda x: x > 0, list_payment):
        new_list.append(i)
    return new_list
