
string = "Hello, World!"


def sequence_buttons(string):

    
    buttons = ".,?!:abcdefghijklmnopqrstuvwxyz "
    translation = (
        "1", "11", "111", "1111", "11111",
        "2", "22", "222", "3", "33", "333",
        "4", "44", "444", "5", "55", "555",
        "6", "66", "666", "7", "77", "777", "7777",
        "8", "88", "888", "9", "99", "999", "9999", "0"
    )

    TRANS = {}

    for c, l in zip(buttons, translation):
        TRANS[ord(c)] = l

    return string.lower().translate(TRANS)


print(sequence_buttons(string))
