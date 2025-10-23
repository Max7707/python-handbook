class Stack:

    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        return self.s.pop()
    
    def is_empty(self):
        if len(self.s) == 0:
            return True
        else:
            return False
        


stack = Stack()
for item in ("Hello,", "world!"):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop())