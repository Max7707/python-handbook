from hashlib import sha256


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(
    password,
    min_length=8,
    possible_chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    at_least_one=str.isdigit,
):
    if not isinstance(password, str):
        raise TypeError
    else:
        if len(password) < min_length:
            raise MinLengthError
        else:
            if not all(ch in possible_chars for ch in password):
                raise PossibleCharError
            else:
                if any(at_least_one(x) for x in password):
                    return sha256(password.encode()).hexdigest()
                else:
                    raise NeedCharError


print(
    password_validation(
        "$uNri$e_777", min_length=6, at_least_one=lambda char: char in "!@#$%^&*()_"
    )
)
