text = 'Alex\nKdfe23\t\f\v.\r'
spec = {'\n', '\t', '\f', '\v', '\r'}


def real_len(text):
    i = 0
    real = 0
    while i < len(text):
        ex = text[i]
        if ex in spec:
            i = i+1
        else:
            i = i+1
            real = real+1
    return real


print(real_len(text))
