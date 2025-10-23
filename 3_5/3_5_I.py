f1 = input()
f2 = input()

with open(f1, encoding="UTF-8") as file:
    ans = []
    for line in file:
        ans.append(line.replace("\t", "").split())

with open(f2, "w", encoding="UTF-8") as file_out:
    for i in ans:
        if len(i) > 0:
            print(" ".join(i), file=file_out)