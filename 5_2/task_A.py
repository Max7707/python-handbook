class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def move(self, a, b):
        self.x += a
        self.y += b

    def length(self, other):
        return round(((self.x - other.x)** 2 + (self.y - other.y)** 2) ** 0.5, 2)


first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))