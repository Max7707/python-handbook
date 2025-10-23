first = input()
second = input()
ans = input()
with open(ans, "w", encoding="UTF-8") as file_out:
    with open(first, encoding="UTF-8") as file_in:
        with open(second, encoding="UTf-8") as file_inn:
            words = dict()
            for line in file_in:
                for i in line.rstrip("\n").split():
                    words[i] = 1
            for lines in file_inn:
                for j in lines.strip("\n").split():
                    words[j] = words.get(j, 0) + 1

    for word in sorted(words):
        if words[word] == 1:
            print(word, file=file_out)