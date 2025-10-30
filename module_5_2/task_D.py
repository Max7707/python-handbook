class Fraction:

    def __nod(self, a, b):
        a = abs(a)
        b = abs(b)
        while a != 0 and b != 0:
            if a >= b:
                a = a % b
            else:
                b = b % a
        return a + b

    def __init__(self, *args):
        if len(args) == 2:
            self.num = args[0]
            self.den = args[1]
        elif isinstance(args[0], str):
            if "/" in args[0]:
                self.num = int(args[0].split("/")[0])
                self.den = int(args[0].split("/")[1])
            else:
                self.num = int(args[0])
                self.den = 1
        else:
            self.num = args[0]
            self.den = 1
        self.__update()

    def __flag(self):
        if self.num < 0:
            return -1
        else:
            return 1

    def __update(self):
        nod = self.__nod(self.num, self.den)
        if nod > 1:
            self.num = self.num // nod
            self.den = self.den // nod
        if self.den < 0:
            self.num *= -1
            self.den *= -1

    def numerator(self, number=None):
        if number is None:
            return abs(self.num)
        else:
            self.num = number * self.__flag()
            self.__update()

    def denominator(self, number=None):
        if number is None:
            return self.den
        else:
            self.den = number
            self.__update()

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction('{self.num}/{self.den}')"

    def __neg__(self):
        return Fraction(-self.num, self.den)

    def __add__(self, other):
        if isinstance(other, int):
            return Fraction(self.num + other * self.den, self.den)
        else:
            return Fraction(
                self.num * other.den + self.den * other.num, self.den * other.den
            )

    def __sub__(self, other):
        if isinstance(other, int):
            return Fraction(self.num - other * self.den, self.den)
        else:
            return Fraction(
                self.num * other.den - self.den * other.num, self.den * other.den
            )

    def __iadd__(self, other):
        if isinstance(other, int):
            self.num = self.num + other * self.den
        else:
            self.num = self.num * other.den + self.den * other.num
            self.den = self.den * other.den
        self.__update()
        return self

    def __isub__(self, other):
        if isinstance(other, int):
            self.num = self.num - other * self.den
        else:
            self.num = self.num * other.den - self.den * other.num
            self.den = self.den * other.den
        self.__update()
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            return Fraction(self.num * other, self.den)
        else:
            return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        if isinstance(other, int):
            return Fraction(self.num, self.den * other)
        else:
            return Fraction(self.num * other.den, self.den * other.num)

    def __imul__(self, other):
        if isinstance(other, int):
            self.num = self.num * other
        else:
            self.num = self.num * other.num
            self.den = self.den * other.den
        self.__update()
        return self

    def __itruediv__(self, other):
        if isinstance(other, int):
            self.den = self.den * other
        else:
            self.num = self.num * other.den
            self.den = self.den * other.num
        self.__update()
        return self

    def reverse(self):
        self.num, self.den = self.den, self.num
        self.__update()
        return self

    def __lt__(self, other):
        if isinstance(other, int):
            return self.num < self.den * other
        else:
            return self.num * other.den < other.num * self.den

    def __gt__(self, other):
        if isinstance(other, int):
            return self.num > self.den * other
        else:
            return self.num * other.den > other.num * self.den

    def __le__(self, other):
        if isinstance(other, int):
            return self.num <= self.den * other
        else:
            return self.num * other.den <= other.num * self.den

    def __ge__(self, other):
        if isinstance(other, int):
            return self.num >= self.den * other
        else:
            return self.num * other.den >= other.num * self.den

    def __eq__(self, other):
        if isinstance(other, int):
            return self.num == self.den * other
        else:
            return self.num * other.den == other.num * self.den

    def __ne__(self, other):
        if isinstance(other, int):
            return self.num != self.den * other
        else:
            return self.num * other.den != other.num * self.den

    def __radd__(self, other):
        if isinstance(other, int):
            return Fraction(self.num + other * self.den, self.den)
        else:
            return Fraction(
                self.num * other.den + self.den * other.num, self.den * other.den
            )

    def __rsub__(self, other):
        if isinstance(other, int):
            return Fraction(other * self.den - self.num, self.den)
        else:
            return Fraction(
                self.num * other.den - self.den * other.num, self.den * other.den
            )
        
    def __rmul__(self, other):
        if isinstance(other, int):
            return Fraction(self.num * other, self.den)
        else:
            return Fraction(self.num * other.num, self.den * other.den)
        
    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Fraction(self.den * other, self.num)
        else:
            return Fraction(self.num * other.den, self.den * other.num)

a = Fraction(1, 2)
b = Fraction('2/3')
c, d = map(Fraction.reverse, (3 - a, 2 / b))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)
