from itertools import product

n = (input())
# print("a b c f")
# for a in (0, 1):
#     for b in (0, 1):
#         for c in (0, 1):
#             f = eval(n)
#             f = 1 if f else 0
#             print(a, b, c, f)

print("a b c f")

for a, b, c in product([0, 1], repeat=3):
    f = eval(n)
    f = 1 if f else 0
    print(a, b, c, f)