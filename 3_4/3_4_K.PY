n = int(input())
m = int(input())

s = len(str(n * m))
k = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        k += 1
        n = str(k)
        while len(n) != s:
            n = ' ' + n
        print(n, end=" ")
    print()
