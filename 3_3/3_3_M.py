data = {'a': [100], 'b': [20, 5], 'c': [7, 15, 3]}

min_vs = []
for value in data.values():
    min_vs.append(sum(value))

min_v = min(min_vs)

for i in data:
    if sum(data[i]) == min_v:
        print(i)
        break


print(min((sum(number), key) for key, number in data.items())[1])