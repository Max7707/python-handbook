text = input()
ans = ""

for i in range(len(text)):
    if text[i] in "0123456789":
        ans += text[i]

print(ans)


ans2 = "".join([text[i] for i in range(len(text)) if text[i] in "0123456789"])
print(ans2)