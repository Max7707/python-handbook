def cycle(n):
    while True:
        for i in range(len(n)):
            s = i % len(n)
            yield n[s]


print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))