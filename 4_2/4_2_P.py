def login(username, password, on_login, on_fail):
    correct_p = hex(sum(ord(i) for i in username) * len(username))[2::][::-1].upper()
    if password == correct_p:
        return on_login(username)
    else:
        return on_fail(username)


def on_login(username):
    print(f'Hello, {username}!')


def on_fail(username):
    print(f'Nice try... You are not {username}!')


login('NoobMaster', '4C72', on_login, on_fail)