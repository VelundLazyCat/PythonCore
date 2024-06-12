from collections import UserString

stroka = '1hjk671l'


class NumberString(UserString):
    def number_summa(self):
        suma = 0
        for i in self.data:
            if i.isdigit():
                suma = suma + int(i)

        return suma

    def number_count(self):
        suma = 0
        for i in self.data:
            if i.isdigit():
                suma = suma + 1

        return suma


sum = NumberString(stroka)

print(sum.number_count())
