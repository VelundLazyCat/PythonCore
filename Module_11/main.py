from collections import UserDict
from datetime import datetime as dt


class Field:
    def __init__(self, value):
        if self.is_valid(value):
            self.__value = value
        else:
            raise ValueError

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value: str):
        if self.is_valid(new_value):
            self.__value = new_value
        else:
            raise ValueError

    def is_valid(self, new_value):
        return True

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):

    def is_valid(self, phone_number: str):
        if (phone_number.isdigit() and len(phone_number) == 10):
            return True
        else:
            return False

    def __repr__(self):
        return str(self.value)


class Birthday(Field):

    def is_valid(self, new_value):
        try:
            if new_value == None:
                return True
            dt.strptime(new_value, '%d.%m.%Y')
            return True
        except ValueError:
            print('Error! date is bad! need format: dd.mm.yyyy')
            return False
        except TypeError:
            return False

    def __str__(self):
        if self.value:
            return str(self.value)


class Record:

    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)
        return phone

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone_number == phone.value:
                self.phones.remove(phone)
                return phone

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone_number == phone.value:
                print(self.name, ': ', phone_number)
                return phone

    def edit_phone(self, phone_number, phone_number_new):
        self.remove_phone(phone_number)
        self.add_phone(phone_number_new)

    def days_to_birthday(self):
        if self.birthday == None:
            return None
        current_datetime = dt.now()    # День відліку
        bday = dt.strptime(self.birthday.value, '%d.%m.%Y')
        temp = dt(current_datetime.year,
                  bday.month, bday.day)
        temp_future = dt(current_datetime.year+1,
                         bday.month, bday.day)
        difference = temp.date()-current_datetime.date()
        difference1 = temp_future.date()-current_datetime.date()
        if difference.days > 0:
            return str(difference.days)
        else:
            return str(difference1.days)

    def __str__(self):
        return f"Contact name: {self.name}, birthday: {self.birthday.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # реалізація класу

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        return self.data.pop(name, None)

    def iterator(self, n=5):
        records = list(self.data.values())
        for i in range(0, len(records), n):
            yield records[i:i+n]

    def __str__(self) -> str:
        return '\n'.join(str(rec) for rec in self.data.values())


if __name__ == '__main__':

    book = AddressBook()
    john_record = Record("John")
    john_record.add_phone("1234567890")
    # john_record.add_phone("17234567890")
    john_record.add_phone("5555555555")
    print(john_record.name)
    print(john_record.phones)
    # john_record.remove_phone('0987654321')

    # Додавання запису John до адресної книги
    book.add_record(john_record)
    print(book.data['John'])

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: <{found_phone}>")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
