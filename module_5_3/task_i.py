import re


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def user_validation(last_name=None, first_name=None, username=None, **kwargs):
    if (last_name is None or first_name is None or username is None) or kwargs:
        raise KeyError
    else:
        if not all(isinstance(x, str) for x in (last_name, first_name, username)):
            raise TypeError
        else:
            ans = dict()
            if re.fullmatch(r"[а-яА-яёЁ]+", last_name):
                if last_name[0].isupper() and last_name[1:].islower():
                    ans["last_name"] = last_name
                else:
                    raise CapitalError
            else:
                raise CyrillicError

            if re.fullmatch(r"[а-яА-яёЁ]+", first_name):
                if first_name[0].isupper() and first_name[1:].islower():
                    ans["first_name"] = first_name
                else:
                    raise CapitalError
            else:
                raise CyrillicError

            if not re.fullmatch(r"[a-zA-Z\d_]+", username):
                raise BadCharacterError
            if username[0] in "0123456789":
                raise StartsWithDigitError
            ans["username"] = username

    return ans


print(
    user_validation(
        last_name="Иванов", first_name="Иван", username="ivanych45", password="123456"
    )
)
