import json
from sys import stdin

answers = []
for line in stdin:
    answers.append(line.strip("\n"))

with open("scoring.json", encoding="UTF-8") as file:
    ans = []
    for group in json.load(file):
        points = group["points"]
    
        for i in group["tests"]:
            ans.append((i["pattern"], points//len(group["tests"])))

answer = 0
for j in range(len(answers)):
    if answers[j] == ans[j][0]:
        answer += ans[j][1]
print(answer)
        
