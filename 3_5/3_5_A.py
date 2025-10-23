from sys import stdin

a = []
for i in stdin:
    a += (i.rstrip("\n").split())

ans = 0
for j in a:
    ans += int(j)
print(ans) 