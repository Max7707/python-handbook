class Rectangle:

    def __init__(self, first, second):
        self.first = list(first)
        self.second = list(second)
        self.update()

    def update(self):
        self.x = round(abs(self.first[0] - self.second[0]), 2)
        self.y = round(abs(self.first[1] - self.second[1]), 2)
        self.max_y = max(self.first[1], self.second[1])
        self.min_x = min(self.first[0], self.second[0])
        self.max_x = max(self.first[0], self.second[0])
        self.min_y = min(self.first[1], self.second[1])
    
    def perimeter(self):
        return round(2*(self.x + self.y), 2)
    
    def area(self):
        return round(self.x * self.y, 2)

    def get_pos(self):
        return (self.min_x, self.max_y)
    
    def get_size(self):
        return (self.x, self.y)
    
    def move(self, dx, dy):
        self.first = [round(self.first[0] + dx, 2), round(self.first[1] + dy, 2)]
        self.second = [round(self.second[0] + dx, 2), round(self.second[1] + dy, 2)]
        self.update()

    def resize(self, width, height):
        top_left = self.get_pos()
        self.first = [top_left[0], top_left[1]]
        self.second = [top_left[0] + width, top_left[1] - height]
        self.update()

    def turn(self):
        x_centr = round(self.min_x + self.x / 2, 2)
        y_centr = round(self.min_y + self.y / 2, 2)

        self.x, self.y = self.y, self.x

        self.first = [round(x_centr - self.x / 2, 2), round(y_centr + self.y / 2, 2)]
        self.second = [round(x_centr + self.x / 2, 2), round(y_centr - self.y / 2, 2)]
        self.update()

    def scale(self, factor):
        x_centr = round(self.min_x + self.x / 2, 2)
        y_centr = round(self.min_y + self.y / 2, 2)

        self.first = [round(x_centr - factor * self.x / 2, 2), round(y_centr + factor * self.y / 2, 2)]
        self.second = [round(x_centr + factor * self.x / 2, 2),  round(y_centr - factor * self.y / 2, 2)]
        self.update()


rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')