import re
path = 'salary.txt'
fh = open(path, 'w')
fh.write("""Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000""")
fh.close()


def total_salary(path):
    summa = 0.0
    salary = 0
    fh = open(path, 'r')
    while True:
        line = fh.readline()
        if not line:
            break
        salary = re.search('\d+', line)
        summa += float(salary.group())

    fh.close()
    return summa


print(total_salary(path))
