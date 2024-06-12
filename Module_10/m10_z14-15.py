class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):

        self.contacts.append({"id": Contacts.current_id, "name": name,
                              "phone": phone, "email": email, "favorite": favorite})
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for cont in self.contacts:
            if cont['id'] == id:
                return cont
        return None


name1 = 'Wylie Pope'
name2 = 'Cyrus Jackson'
phone1 = '(692) 802-2949'
phone2 = '(501) 472-5218'
email1 = 'est@utquamvel.net'
email2 = 'nibh@semsempererat.com'
favorite1 = True
favorite2 = False

cont = Contacts()
cont.add_contacts(name1, phone1, email1, favorite1)
print(cont.list_contacts(), '\n', '-'*10)
cont.add_contacts(name2, phone2, email2, favorite2)
print(cont.list_contacts(), '\n', '-'*10)
print(cont.get_contact_by_id(1), '\n', '-'*10)
