from itertools import chain

products = sorted(set(chain.from_iterable([input().split(", ") for i in range(3)])))


for index, s in enumerate(products, 1):
    print(f"{index}. {s}")
