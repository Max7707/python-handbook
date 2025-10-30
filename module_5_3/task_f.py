from fractions import Fraction


class MyExceptions(Exception):
    pass


class NoSolutionsError(MyExceptions):
    pass


class InfiniteSolutionsError(MyExceptions):
    pass


def is_fraction(x):
    if isinstance(x, (int, Fraction)):
        return True

    try:
        Fraction(x)
        return True

    except Exception:
        return False


def find_roots(a, b, c):
    if all([is_fraction(a), is_fraction(b), is_fraction(c)]):
        if a == b == c == 0:
            raise InfiniteSolutionsError
        elif a == b == 0 and c != 0:
            raise NoSolutionsError
        elif a == 0 and b != 0 and c != 0:
            return ((-c) / b, (-c) / b)

        else:
            d = b**2 - 4 * a * c
            if d >= 0:
                return (((-b) - d**0.5) / (2 * a), ((-b) + d**0.5) / (2 * a))
            else:
                raise NoSolutionsError
    else:
        raise TypeError


print(find_roots(3.1234123512, 6, 2))
