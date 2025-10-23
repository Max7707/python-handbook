import json
from sys import stdin

name_f = input()

with open(name_f, encoding="UTF-8") as file_in:
    content = json.load(file_in)

for i in stdin:
    line = i.rstrip("\n").split(" == ")
    content[line[0]] = line[1]

with open(name_f, "w", encoding="UTF-8") as file_out:
    json.dump(content, file_out, ensure_ascii=False, indent=4)
