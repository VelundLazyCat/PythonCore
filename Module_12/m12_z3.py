import csv

contacts = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False
},
    {
    "name": "Chaim Lewis",
    "email": "dui.in@egetlacus.ca",
    "phone": "(294) 840-6685",
    "favorite": False
},
    {
    "name": "Kennedy Lane",
    "email": "mattis.Cras@nonenimMauris.net",
    "phone": "(542) 451-7038",
    "favorite": True
},
    {
    "name": "Wylie Pope",
    "email": "est@utquamvel.net",
    "phone": "(692) 802-2949",
    "favorite": False
},
    {
    "name": "Cyrus Jackson",
    "email": "nibh@semsempererat.com",
    "phone": "(501) 472-5218",
    "favorite": True
}]

filename = 'test_12_3.csv'

def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fh:
        fields_names = list(contacts[0].keys())
        writer = csv.DictWriter(fh, fieldnames=fields_names)
        writer.writeheader()
        for row in contacts:
            writer.writerow(rowdict=row)


def read_contacts_from_file(filename):
    with open(filename, newline='') as fh:
        temp_contacts = []
        reader = csv.DictReader(fh)
        for row in reader:
            if row['favorite']=='True':
                row['favorite']=row['favorite']=True
            elif row['favorite']=='False':
                row['favorite']=row['favorite']=False
            temp_contacts.append(row)
        return temp_contacts


if __name__=='__main__':
    # write_contacts_to_file(filename, contacts)
    data = read_contacts_from_file(filename)
    print(data==contacts)
