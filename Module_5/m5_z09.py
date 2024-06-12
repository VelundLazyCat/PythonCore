
def formatted_numbers():
    ff = []
    st = ''
    header = '|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary')
    ff.append(header)
    for i in range(16):

        st = '|{:<10d}|{:^10x}|{:>10b}|'.format(i, i, i)
        ff.append(st)
        i = i+1
    return ff


for el in formatted_numbers():
    print(el)
