from sys import stdin

lines = []
for i in stdin:
    lines.append(i.rstrip("\n"))
n = len(lines)

s = 0
for j in lines:
    a = j.split()
    s += int(a[2]) - int(a[1]) 

ans = round(s / n)
print(ans)