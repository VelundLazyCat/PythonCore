import re


def find_all_phones(text):
    result1 = re.findall(r"\+380\(\d{2}\)\d{3}-\d{1}-\d{3}", text)
    result2 = re.findall(r"\+380\(\d{2}\)\d{3}-\d{2}-\d{2}", text)
    return result1+result2
