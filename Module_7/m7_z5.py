# text1 = ' ruad a gosh'
text2 = ' herkk. kwelk efkjwekf ! kfen fhe kk? kjjwe'


def capital_text(s):
    count = 1

    s = s.strip()
    s=s.capitalize()
    s_list = s.split(' ')
    s_list_new = []

    for i in s_list:
        
        if i.endswith('.') or i.endswith('!') or i.endswith('?'):
            s_list[count] = s_list[count].capitalize()
        s_list_new.append(i)
        if count == len(s_list):
            break
        count = count+1

    return ' '.join(s_list_new)


# print(capital_text(text1))
print(capital_text(text2))
