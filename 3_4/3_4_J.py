from itertools import product

n = int(input())
print("А Б В")
for i in product([b for b in range(1, n - 1)], repeat=2):
    if n - i[0] - i [1] >= 1:
        print(*(i + (n - i[0] - i [1], )))