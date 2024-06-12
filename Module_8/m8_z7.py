import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
cats_tuple = [Cat("Mick", 5, "Sara"), Cat(
    "Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]

cats_dict = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]


def convert_list(cats):

    if isinstance(cats[0], tuple):

        return [i._asdict() for i in cats]

    elif isinstance(cats[0], dict):
        cats_list = []

        for j in cats:

            gg = [val for val in j.values()]
            cats_list.append(Cat._make(gg))

        return cats_list


print(convert_list(cats_tuple))
print(convert_list(cats_dict))
