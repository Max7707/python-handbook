words = input()
ans = []
vowels = "аяуюоёэеиыaeiouy"
for i in range(len(words.split())):
    quantity = 0
    for j in range(len(words[i])):
        if words[i].lower()[j] in vowels:
            quantity += 1
        if quantity == 3:
            ans.append(words[i])
            quantity = 0

print(ans)


ans2 = [word for word in words.split() if len([letter for letter in word.lower() if letter in "аяуюоёэеиыaeiouy"]) >= 3]
print(ans2)