
path = 'employees.txt'


def read_employees_from_file(path):
    employ = []
    fh = open(path, 'r')
    while True:
        line = fh.readline()
        if not line:
            break
        line = line.removesuffix('\n')
        employ.append(line)
    fh.close()
    return employ


print(read_employees_from_file(path))

