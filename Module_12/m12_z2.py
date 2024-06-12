import json


def write_contacts_to_file(filename, contacts):
    with open(filename, "w") as file:

        json.dump({"contacts": contacts}, file, indent=4)


def read_contacts_from_file(filename):
    with open(filename, "r") as fh:
        unpacked = json.load(fh)
    return unpacked["contacts"]
