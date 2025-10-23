from itertools import product

n = input()
a = set()
for k in n:
    if k.isupper():
        a.add(k)
s = sorted(list(a))
print(*(s), "F")

n = n.split()

if "~" in n:
    ans1 = ["("]
    ans2 = []
    for i in n:
        if i != "~":
            ans1.append(i)
        elif i == "~":
            break
    ans1.append(") ~ ")

    for i in n[::-1]:
        if i != "~":
            ans2 = [i] + ans2
        elif i == "~":
            break
    ans2 = ["("] + ans2 + [")"]

ans3 = ans1 + ans2
ans = " ".join(ans3)
ans = ans.replace("~", "==").replace("->", "<=").replace("^", "!=")

for j in product([0, 1], repeat=len(s)):
    x = {key: value for key, value in zip(s, j)}
    print(*(m for m in j), int(eval(ans, x)))

