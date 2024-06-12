contacts = {}
flag = False


def input_error(func):
    def inner(comand_word, data):

        data = data.split(' ')
        if comand_word == 'add' and len(data) <= 1:
            print('The data is not enough')
            print("Give me name and phone please")
        elif comand_word == 'add' and contacts.get(data[0]):
            print('This contact already exist')
        elif comand_word == 'change' and len(data) <= 1:
            print('The data is not enough')
            print("Give me name and phone please")
        elif comand_word == 'show all' and len(contacts) == 0:
            print('Contacts not founds')
        elif comand_word == 'phone' and not contacts.get(data[0]):
            print(f'Contact {data[0]} not found')
            print("Enter user name Please")
        else:
            result = func(comand_word, data)
            return result

    return inner


def say_hello(comand_word, data):
    print("How can I help you?")
    return False


def good_bye(comand_word, data):
    print("Good bye!")
    input('Press any Enter please...')
    return True


@input_error
def add_contact(comand_word, data):
    contacts.update({data[0]: data[1]})
    print(f'New contact: {data[0]}, phone:{data[1]}')
    return False


@input_error
def do_change(comand_word, data):
    contacts[data[0]] = data[1]
    print(f'Contact {data[0]} has been changed')
    return False


@input_error
def show_phone(comand_word, data):
    print(f' Phone of {data[0]} is: {contacts[data[0]]}')
    return False


@input_error
def show_all(comand_word, data):
    for keys, values in contacts.items():
        print(keys, ':   ', values)
    return False


COMMANDS = {'hello': say_hello, 'add': add_contact,
            'change': do_change, 'phone': show_phone,
            'show all': show_all, 'good bye': good_bye,
            'close': good_bye, 'exit': good_bye}


def get_handler(operator):
    return COMMANDS[operator]


def parser_comand(data):
    for keys in COMMANDS:
        print(data.lower().find(keys))
        if data.lower().find(keys) >= 0:
            data_output = data[data.lower().find(keys)+len(keys):]
            return keys, data_output.strip()

    return None, None


if __name__ == "__main__":

    while not flag:

        input_command = input('Enter command please:\n>>>')
        comand_word, comand_data = parser_comand(input_command)

        if COMMANDS.get(comand_word):
            flag = get_handler(comand_word)(comand_word, comand_data)
        else:
            print('Command unknown. Try else')
