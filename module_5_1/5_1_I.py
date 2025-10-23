class Queue:

    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        return self.s.pop(0)
    
    def is_empty(self):
        if len(self.s) == 0:
            return True
        else:
            return False
        
    
queue = Queue()
for item in ("Hello,", "world!"):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop())