class Myclass:
    def __repr__(self):
        raise Exception
    

def func(a, b, c):
    return ''.join(map(str, (a, b, c)))


a = Myclass()
print(func(a))