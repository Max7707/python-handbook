class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, a, b):
        self.x += a
        self.y += b

    def length(self, other):
        return round(((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5, 2)

    def __str__(self):
        return f"{self.x, self.y}"


class PatchedPoint(Point):

    def __init__(self, *args):
        if args and isinstance(args[0], tuple):
            super().__init__(args[0][0], args[0][1])
        else:
            super().__init__(*args)

    def __repr__(self):
        return f"PatchedPoint{self.x, self.y}"

    def __str__(self):
        return f"{self.x, self.y}"

    def __add__(self, other):
        new_point = Point(self.x + other[0], self.y + other[1])
        return new_point

    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self


first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)
