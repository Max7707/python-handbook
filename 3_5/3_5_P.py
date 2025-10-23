from sys import stdin

user_input = " ".join(input().split()).lower()

files = []
for file in stdin:
    files.append(file.strip("\n"))

ans = 0
for i in files:
    with open(i, encoding="UTF-8") as file_in:
        first = " ".join(file_in.read().split()).lower()
        if user_input in first:
            print(i)
            ans += 1

if ans == 0:
    print("404. Not Found")
