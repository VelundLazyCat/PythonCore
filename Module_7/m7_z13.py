def get_employees_by_profession(path, profession):

    new_line = []
    with open(path, 'r') as fh:
        lines = fh.readlines()

    for line in lines:
        if line.find(profession) >= 0:

            line = line.removesuffix('\n')
            line = line.replace(profession, "")
            line = line.rstrip()
            new_line.append(line)

    return ' '.join(new_line)
