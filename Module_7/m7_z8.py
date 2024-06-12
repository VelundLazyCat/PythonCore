import re
viraz = "2+ (34-5) * 3"


def token_parser(s):

    symbols = ('+','-','*','/','(',')')
    new_data = []
    s = re.sub(r' ', '', s)

    numbers = re.findall('\d+', s)
    i=0
    

    while len(s)>0:
        if s[0] in symbols:
            new_data.append(s[0])
            s=s[1:]
                       
        else: 
            new_data.append(numbers[i])
            s=s.removeprefix(numbers[i])
            i+=1

    return new_data
 
            

    

print(token_parser(viraz))




