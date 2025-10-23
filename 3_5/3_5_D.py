from sys import stdin

basic = []
for i in stdin:
    basic.append(i.rstrip("\n"))

search = basic.pop(-1).lower()

for j in basic:
    if search in j.lower():
        print(j)
    