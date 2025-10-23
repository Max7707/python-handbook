from itertools import cycle

ppgs = [input() for i in range(int(input()))]
stop = int(input())
count = 0
for porridge in cycle(ppgs):
    print(porridge)
    count += 1
    if count == stop:
        break