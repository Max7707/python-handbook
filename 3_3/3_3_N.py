data = {'a': [1, 2, 1], 'b': [2, 3, 2, 5, 1]}

ans = set()
for key, number in data.items():
    for i in number:
        if number.count(i) > 1:
            ans.add(key)

print(ans)


print({k for k, number in data.items() for j in number if number.count(j) > 1})