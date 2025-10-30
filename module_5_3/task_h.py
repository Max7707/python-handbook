import re


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(un):
    if not isinstance(un, str):
        raise TypeError

    if not re.fullmatch(r"[a-zA-Z\d_]+", un):
        raise BadCharacterError

    if un[0] in "0123456789":
        raise StartsWithDigitError

    return un


print(username_validation(123))
