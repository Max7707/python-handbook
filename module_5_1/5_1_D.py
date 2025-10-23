class Programmer:
    positions = {"Junior": 10, "Middle": 15, "Senior": 20}
    posts = ["Junior", "Middle", "Senior"]
    def __init__(self, name, post):
        self.name = name
        self.post = post
        self.worktime = 0
        self.salary = Programmer.positions[post]
        self.earned = 0

    def work(self, time):
        self.worktime += time
        self.earned += time * self.salary

    def rise(self):
        i = Programmer.posts.index(self.post)
        if i < 2:
            i += 1
            self.post = Programmer.posts[i]
            self.salary = Programmer.positions[self.post]
        else:
            self.salary += 1

    def info(self):
        return f"{self.name} {self.worktime}ч. {self.earned}тгр."
        

programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())