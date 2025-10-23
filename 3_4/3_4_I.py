from itertools import product, islice

s = int(input())
xy = [x * y for x, y in product([i for i in range(1, s + 1)], repeat=2)]

for i in range(s):
    print(*islice(xy, i * s, (i + 1) * s))

