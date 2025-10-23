numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 112, 13}

ans = set()


for i in numbers:
    if i == 1 or i == 0:
        continue
    if i == 2:
        ans.add(i)
        continue
    divs = 0
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            divs += 1
    if divs == 0:
        ans.add(i)

print(ans)


ans2 = {n for n in numbers if all(n % k != 0 for k in range(2, int(n ** 0.5) + 1)) if n > 1}
print(ans2)