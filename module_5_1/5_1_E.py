class Rectangle:

    def __init__(self, first, second):
        self.a = abs(first[0] - second[0])
        self.b = abs(first[1] - second[1])

    def perimeter(self):
        return round(2*(self.a + self.b), 2)
    
    def area(self):
        return round(self.a * self.b, 2)
    

rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())