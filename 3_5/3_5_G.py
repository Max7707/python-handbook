file = input()

with open(file, "r", encoding="UTF-8") as file_in:
    numbers = []
    for line in file_in:
        numbers += line.split()
    print(len(numbers))
    
    cnt = 0
    for j in numbers:
        if int(j) > 0:
            cnt += 1
    print(cnt)

    i_numb = []
    for i in numbers:
        i_numb.append(int(i))

    print(min(i_numb))

    print(max(i_numb))

    print(sum(i_numb))

    print(round(sum(i_numb) / len(i_numb), 2))