import sys
import os
import pickle
from dataclasses import AddressBook, Record, Phone


class Bot:

    def __init__(self) -> None:

        self.file_contacts = 'contacts.pkl'
        self.adressbook = AddressBook()
        try:
            with open(self.file_contacts, 'rb') as file:
                contacts_load = pickle.load(file)
                self.adressbook.data = contacts_load
        except:
            print('New adressbook created')

    @staticmethod
    def input_error(func):
        """ Функція  декоратор обробки помилок """
        def wrapper(*args):
            try:
                return func(*args)
            except KeyError as err:
                if str(err) == "Command not found":
                    print("Command not found")
                    return
                print("Enter user name please")
            except ValueError as err:
                if str(err) == "Contact already exist.":
                    print(
                        "Contact already exist. Use 'change' coomand to update the phone number.")
                    return
                print(err)
            except IndexError:
                print("Contacts not founds")
        return wrapper

    def save_addressbook(self):
        with open(self.file_contacts, 'wb') as file:
            pickle.dump(self.adressbook.data, file)

    def say_hello(self, _):
        """ Функція привітання по кодовому слову 'hello' """
        print("How can I help you?")

    def good_bye(self, _):
        """ Функція виходу з програми """
        self.save_addressbook()
        input('Good bye!\nPress any Enter please...')
        sys.exit()

    @input_error
    def add_contact(self, data):
        """ функція створення нового контакта """
        if not data.strip():
            raise ValueError('No name and telephone')
        new_name, phone_number = data.split()
        if new_name in self.adressbook.data.keys():
            raise ValueError("Contact already exist.")
        record = Record(new_name)
        record.add_phone(phone_number)
        self.adressbook.add_record(record)
        print(f"Contact {new_name} added successfully")
        # может вернуть строку которую принтануть?
        return record

    @input_error
    def search_contact(self, data):
        result = []
        if not data.strip():
            raise ValueError
        for record in self.adressbook.data.values():
            record_string = record.name.value.lower(
            ) + ' '.join([phone.value for phone in record.phones])
            if data.lower() in record_string:
                result.append(record)
        if not result:
            raise ValueError("Contacts not found")
        print('\n'.join(str(rec) for rec in result))
        return result

    @input_error
    def change_phone(self, data):
        if not data.strip():
            raise ValueError(
                "No data. Please write name telephone to change and new telephon")
        name, old_phone, new_phone = data.split()
        if name not in self.adressbook.data.keys():
            raise ValueError(f"Contact <{name}> not found.")
        change_record = self.adressbook.data[name]
        old_phone, new_phone = Phone(old_phone), Phone(new_phone)
        for ph in change_record.phones:
            if old_phone.value == ph.value:
                ph.value = new_phone.value
                print(f'Contact {name} has been changed')
                break

    @input_error
    def show_all(self, _):
        if not self.adressbook.data:
            return "No contacts available"
        result = self.adressbook
        print(result)
        return result

    COMMANDS = {'hello': say_hello,      'add': add_contact,
                'change': change_phone,  'search': search_contact,
                'show all': show_all,    'good bye': good_bye,
                'close': good_bye,    'exit': good_bye}

    @input_error
    def parser_comand(self, data):
        data = data.strip()
        if not data:
            raise ValueError("Command not found")
        for key in self.COMMANDS:
            if not data.lower().find(key):
                data = data[len(key):].strip()
                if not data:
                    data == None
                return key, data
        raise KeyError("Command not found")

    def get_handler(self, operator):
        return self.COMMANDS[operator]

    def run(self):
        while True:
            input_command = input('Enter command please:\n>>>')
            comand_word, comand_data = self.parser_comand(input_command)
            self.get_handler(comand_word)(self, comand_data)


if __name__ == '__main__':
    bot = Bot()
    bot.run()
