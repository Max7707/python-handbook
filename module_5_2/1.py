def nod(a, b):
    a = abs(a)
    b = abs(b)
    while  a != 0 and b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a + b

print(nod(-14, -35))

print(isinstance(-1, int))