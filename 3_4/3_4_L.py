s = []
for i in range(int(input())):
    for j in (input().split(", ")):
        s.append(j)

for index, value in enumerate(sorted(s), 1):
    print(f"{index}. {value}")

