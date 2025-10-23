numbers = {2, 4, 5, 7, -10, -8, 10, -9, -1}
ans = []
for i in numbers:
    for j in numbers:
        if i != j:
            ans.append(i * j)


print(ans)


ans2 = max(k * p for k in numbers for p in numbers if k != p)
print(ans2)