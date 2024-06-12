
data = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
data1 = "XXXZZXXYYYZZ"


def encode(data):
    if len(data) == 0:
        return []
    if not data:
        return ''
    else:
        char = data[0]
        max_index = len(data)
        i = 1
        while i < max_index and char == data[i]:
            i += 1
        return [char]+[i] + encode(data[i:])


print(encode(data))
