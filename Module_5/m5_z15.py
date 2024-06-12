import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"\bhttps?://\w+.{1}\w+.{1}\w{3}\b", text)
    for match in iterator:
        result.append(match.group())
    return result
