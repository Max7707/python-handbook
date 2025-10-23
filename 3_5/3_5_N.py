import json

file_1 = input()
file_2 = input()

with open(file_1, encoding="UTF-8") as file_in:
    content = json.load(file_in) 

with open(file_2, encoding="UTF-8") as file_in1:
    new = json.load(file_in1)

ans = dict()
for i in content:
    ans[i.pop("name")] = i

new_apd = dict()
for k in new:
    new_apd[k.pop("name")] = k

for n in new_apd:
    for j in new_apd[n]:
        if j in ans[n]:
            ans[n][j] = (max(ans[n][j], new_apd[n][j]))
        else:
            ans[n][j] = new_apd[n][j]
            
with open(file_1, "w", encoding="UTF-8") as file_out:
    json.dump(ans, file_out, ensure_ascii=False, indent=4)