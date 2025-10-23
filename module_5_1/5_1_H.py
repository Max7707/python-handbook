class Cell:

    def __init__(self, state):
        self.state = state

    def status(self):
        return self.state
    

class Checkers:
    def __init__(self):
        self.desk = dict()
        width = "ABCDEFGH"
        height = "87654321"
        for i in range(len(height)):
            for j in range(len(width)):
                if (i + j) % 2 != 0:
                    if height[i] in "678":
                        self.desk[width[j] + height[i]] = Cell("B")
                    elif height[i] in "123":
                        self.desk[width[j] + height[i]] = Cell("W")
                    else:
                        self.desk[width[j] + height[i]] = Cell("X")
                else:
                    self.desk[width[j] + height[i]] = Cell("X")
    
    def move(self, f, t):
        self.desk[t] = self.desk[f]
        self.desk[f] = Cell("X")
    
    def get_cell(self, p):
        return self.desk[p]


checkers = Checkers()
checkers.move('C3', 'D4')
checkers.move('H6', 'G5')
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()