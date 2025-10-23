import json

file = input()
file1 = input()

ans = dict()
with open(file, encoding="UTF-8") as file_in:
    numbers = []
    for line in file_in:
        numbers += line.split()
    
    ans["count"] = len(numbers)
    
    pos_c = 0
    for i in numbers:
        if int(i) > 0:
            pos_c += 1
    ans["positive_count"] = pos_c
    
    i_numbers = []
    for j in numbers:
        i_numbers.append(int(j))

    ans["min"] = min(i_numbers)
    ans["max"] = max(i_numbers)
    ans["sum"] = sum(i_numbers)
    ans["average"] = round(sum(i_numbers) / len(i_numbers), 2)


with open(file1, "w", encoding="UTF-8") as file_out:
    json.dump(ans, file_out, indent=4)  
