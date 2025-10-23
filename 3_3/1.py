# n = input()
# for i in range(len(n)):
#     if n[i] == "~":
#        n[i - 1] = ')' 

# n = n.replace("^", "!=").replace("->", "<=").replace("~", "==")
# print(n)

n = "A -> B ~ C"
s = n.split()
print(s)

if "~" in n:
    ans1 = ["("]
    ans2 = ["("]
    for i in s:
        if i != "~":
            ans1.append(i)
        elif i == "~":
            break
    ans1.append(") ~ ")

    for i in s[::-1]:
        if i != "~":
            ans2.append(i)
        elif i == "~":
            break
    ans2.append(")")

ans1 = " ".join(ans1)
ans2 = " ".join(ans2)
ans = ans1 + ans2
print(ans1)     
print(ans2)   
print(ans)
