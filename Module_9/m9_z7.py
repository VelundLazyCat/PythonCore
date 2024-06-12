name = ["dan", "jane", "steve", "mike"]


def normal_name(list_name):
    return [name.capitalize() for name in list_name]


def normal_name1(list_name):
    new_list = []
    for i in map(lambda name: name.capitalize(), list_name):
        new_list.append(i)
    return new_list


print(normal_name(name))
