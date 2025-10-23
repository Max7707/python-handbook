numbers = list(input())
ans = set()
for i in numbers:
    if numbers.count(i) == 1:
        ans.add(i)

print(ans)


ans2 = set(i for i in numbers if numbers.count(i) == 1)
print(ans2)