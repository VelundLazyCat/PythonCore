
path = 'employees.txt'
employ = [['Robert Stivenson,28', 'Alex Denver,30'],
          ['Drake Mikelsson,19', 'John Do,88']]


def write_employees_to_file(employee_list, path):

    fh = open(path, 'w')
    for otdel in employee_list:
        for i in otdel:
            fh.write(i+'\n')

    fh.close()


write_employees_to_file(employ, path)
