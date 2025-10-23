a = int(input())
b = int(input())

ans = []
if a > b:
    for i in range(a, b - 1, -1):
        ans.append(i ** 2)

else:
    for i in range(a, b + 1):
        ans.append(i ** 2)
print(ans)

ans1 = [number ** 2 for number in range(a, b + 1 if a <= b else b - 1, 1 if a <= b else -1)]
print(ans1)