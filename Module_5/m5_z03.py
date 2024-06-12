def sanitize_phone_number(phone):
    del_set = {' ', '(', ')', '-', '+'}
    new_phone = ''
    phone = phone.strip()
    for item in phone:
        if item in del_set:
            item = ''
            new_phone = new_phone+item
        else:
            new_phone = new_phone+item
    return new_phone
def sanitize_phone_number1(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone
