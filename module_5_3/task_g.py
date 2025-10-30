import re


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError

    if re.fullmatch(r"[а-яА-яёЁ]+", name):
        if name[0].isupper() and name[1:].islower():
            return name
        else:
            raise CapitalError
    else:
        raise CyrillicError


print(name_validation("иванов"))
