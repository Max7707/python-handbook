from itertools import combinations

for game in combinations([input() for i in range(int(input()))], 2):
    print(f"{game[0]} - {game[1]}")
