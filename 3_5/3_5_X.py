with open('another_file.txt', 'rb') as file:
    b = file.read()
    s = len(b)

a = ["Б", "КБ", "МБ", "ГБ"]
ind_a = 0

while s >= 1024 and ind_a != 3:
    s /= 1024
    if s % 1 != 0:
        s += 1
    ind_a += 1

print(f"{s}{a[ind_a]}")