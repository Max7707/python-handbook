from itertools import product, combinations

suit = input()
value = input()

suits = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
values = ["10", "2", "3", "4", "5", "6", "7", "8", "9", "валет", "дама", "король", "туз"]

deck = []
for i in product(values, suits.values()):
    deck.append(" ".join(i))

cnt = 0
answ = []
for j in combinations(deck, 3):
    ans = ", ".join(j)
    if suits[suit] in ans and value not in ans:
        answ.append(ans)
    if len(answ) == 10:
        break

for k in answ:
    print(k)