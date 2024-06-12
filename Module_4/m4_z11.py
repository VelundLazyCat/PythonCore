from random import randint

numbers={'0','1','2','3','4','5','6','7','8','9'}
password='z,qrE*IE'
def is_valid_password(password):
    is_number=False
    is_big_bukva=False
    is_small_bukva=False

    if len(password)==8:
        for i in password:
            if i in numbers:
                is_number=True
                
            if ord(i)<123 and ord(i)>96: 
                is_small_bukva=True
                
            if ord(i)>64 and ord(i)<90:
                is_big_bukva=True
                
    return is_number & is_big_bukva & is_small_bukva
    

print(is_valid_password(password))



def is_valid_password1(password):
    if len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_num = True

    return has_upper and has_lower and has_num
def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result