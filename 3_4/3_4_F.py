suit = ["пик", "треф", "бубен", "червей"]
den = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]

from itertools import product

suit.remove(input())
for value in product(den, suit):
    print(f"{value[0]} {value[1]}")