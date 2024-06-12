pin = ['1101', '9034', '00112']


def is_valid_pin_codes(pin_codes):
    is_pin = False
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    set_pin_codes = set(pin_codes)
    if len(pin_codes) != 0 and len(set_pin_codes) == len(pin_codes):
        for i in pin_codes:
            if len(i) == 4:
                for j in i:
                    if set(j) & numbers:
                        is_pin = True
                    else:
                        is_pin = False
                        break
            else:
                is_pin = False
                break

    else:
        is_pin = False

    return is_pin


print(is_valid_pin_codes(pin))
