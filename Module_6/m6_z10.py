path_user = 'users_pass.txt'
users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}


def save_credentials_users(path, users_info):
    with open(path, 'wb') as fh:
        for key, val in users_info.items():
            fh.write(bytes(f'{key}:{val}\n', 'utf-8'))


save_credentials_users(path_user, users_info)
