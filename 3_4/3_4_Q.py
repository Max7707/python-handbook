from itertools import product, combinations

suit = input()
nv = input()
lstr = input()

suits = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
values = ["10", "2", "3", "4", "5", "6", "7", "8", "9", "валет", "дама", "король", "туз"]

deck = []
for v, s in product(values, suits.values()):
    deck.append(v + " " + s)

threes = []
for i in combinations(deck, 3):
    threes.append(", ".join(i))
    
n = threes.index(lstr)

for j in range(n + 1, len(threes)):
    if suits[suit] in threes[j] and nv not in threes[j]:
        print(threes[j])
        break