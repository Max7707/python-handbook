from itertools import permutations

lop = []
for i in range(int(input())):
    product = input()
    lop.extend(product.split(", "))

for j in permutations(sorted(lop), 3):
    print(*j)

