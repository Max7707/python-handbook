from sys import stdin

lines = []
for i in stdin:
    lines.append(i.rstrip("\n"))

ans = []
for j in lines:
    if "#" in j:
        if j.index("#") == 0:
            None
        else:
            print(j[:j.index("#") - 1])
    else:
        print(j)

