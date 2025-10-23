from itertools import product

n = input()
a = set()
for i in n:
    if i.isupper():
        a.add(i)

s = sorted(list(a))
print(*s, "F")

for j in product([0, 1], repeat=len(s)):
    x = {key: value for key, value in zip(s, j)}
    print(*(m for m in j), int(eval(n, x)))