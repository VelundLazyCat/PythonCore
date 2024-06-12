def get_favorites(contacts):
    new_list = []
    for i in filter(lambda x: x["favorite"], contacts):
        new_list.append(i)
    return new_list
