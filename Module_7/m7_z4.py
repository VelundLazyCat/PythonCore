
cyfra0 = '1263'
cyfra1 = '  +1263 '
cyfra2 = '  +12yi63 '
cyfra3 = '     '
cyfra4 = ''


def is_integer(s):
    s = s.strip()

    if len(s) == 0:

        return False

    if s[0] == "+" or s[0] == "-":
        s = s[1:]

    return s.isdigit()


print(is_integer(cyfra0))
print(is_integer(cyfra1))
print(is_integer(cyfra2))
print(is_integer(cyfra3))
print(is_integer(cyfra4))
