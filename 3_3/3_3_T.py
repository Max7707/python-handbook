text = 'ехали медведи на велосипеде'

ans = set()
for word in text.split():
    for word2 in text.split():
        if word != word2:
            general = set(word) & set(word2)
            if len(general) > 2:
                pair = tuple(sorted([word, word2]))
                ans.add(pair)
print(ans)



ans2 = {tuple(sorted([w1, w2])) for w1 in text.split() for w2 in text.split() if w1 != w2 and len(set(w1) & set(w2)) > 2}
print(ans2)