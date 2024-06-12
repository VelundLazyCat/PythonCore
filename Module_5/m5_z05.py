list_phones = ['380998759405', '818765347', '8867658976', '657658976']


def get_phone_numbers_for_countries(list_phones):
    phone_number = {'UA': [], 'JP': [], 'TW': [], 'SG': []}
    ua_nlp = []
    jp_nlp = []
    tw_nlp = []
    sg_nlp = []
    for phone in list_phones:
        if phone.startswith('81'):
            jp_nlp.append(phone)
            phone_number['JP'] = jp_nlp
        elif phone.startswith('65'):
            sg_nlp.append(phone)
            phone_number['SG'] = sg_nlp
        elif phone.startswith('886'):
            tw_nlp.append(phone)
            phone_number['TW'] = tw_nlp
        else:
            ua_nlp.append(phone)
            phone_number['UA'] = ua_nlp
    return phone_number


print(get_phone_numbers_for_countries(list_phones))
