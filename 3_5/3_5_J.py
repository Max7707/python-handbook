file = input()
n = int(input())

with open(file, encoding="UTF-8") as file_in:
    ans = []
    for line in file_in:
        ans.append(line.rstrip("\n"))

    for i in range(len(ans) - n, len(ans)):
        print(ans[i])