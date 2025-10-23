from itertools import count

text = input().split()
for value in count(float(text[0]), float(text[2])):
    if value >= float(text[1]):
        break
    print(round(value, 2))