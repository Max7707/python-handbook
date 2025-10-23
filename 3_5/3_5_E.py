from sys import stdin

d = []

for i in stdin:
    d += i.rstrip("\n").split()

for j in sorted(set(d)):
    if j.lower() == j[::-1].lower():
        print(j)