import re
abituery = [{
    "name": "Kovalchuk Oleksiy",
    "specialty": 301,
    "math": 175,
    "lang": 180,
    "eng": 155,
},
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
},
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
}]
file_name = 'abituery.txt'


def save_applicant_data(source, output):
    i = 0

    with open(output, 'w') as fh:
        for item in source:
            i += 1
            student_date = ''
            for val in item.values():
                student_date += f'{val},'
            student_date = student_date.removesuffix(',')
            fh.write(student_date)
            if i < len(source):
                fh.write('\n')


def save_applicant_data1(source, output):
    lines = []
    for item in source:

        lines.append([str(val) for val in item.values()])

    with open(output, 'w') as fh:
        for line in lines:
            fh.write(','.join(line)+'\n')


save_applicant_data(abituery, file_name)
