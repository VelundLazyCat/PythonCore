import re


def find_all_emails(text):
    result = re.findall(r"[a-zA-Z]+[\w.-]+@[a-zA-Z-]+\.[\w]+[\w]+", text)
    return result
