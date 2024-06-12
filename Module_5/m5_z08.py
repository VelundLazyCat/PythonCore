grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}


def formatted_grades(students):
    i = 0
    ff = []
    st = ''
    for st in students:
        i = i+1
        st = '{:>4}|{:<10}|{:^5}|{:^5}'.format(
            i, st, students[st], grades[students[st]])
        ff.append(st)
    return ff


formatted_grades(students)
