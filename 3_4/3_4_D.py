from itertools import accumulate

for value in accumulate(word + " " for word in input().split()):
    print(f"{value}")