from itertools import permutations

n = int(input())
names = []
for i in range(n):
    name = input()
    names.append(name)

for j in permutations(sorted(names), 3):
        print(", ".join(j))