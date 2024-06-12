contacts = [{
    "name": "Raymond",
    "email": "halla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},
    {"name": "Allen",
     "email": "nulla.ante@vestibul.co.uk",
     "phone": "(992) 914-3792",
     "favorite": False, }]


def get_emails(list_contacts):
    new_list = []

    for new in map(lambda x: x["email"], list_contacts):
        new_list.append(new)

    return new_list


print(get_emails(contacts))
