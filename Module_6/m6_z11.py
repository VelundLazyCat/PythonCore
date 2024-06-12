path_user = 'users_pass.txt'
users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}


def get_credentials_users(path):
    users_lines = []
    with open(path, 'rb') as fh:
        line = fh.read()
        line = line.decode()

    return line.split('\n')


print(get_credentials_users(path_user))
