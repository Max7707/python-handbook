from itertools import permutations 

names = []
for j in range(int(input())):
    name = input()
    names.append(name)

for i in permutations(sorted(names)):
    print(", ".join(i))
