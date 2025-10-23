def f(n):
    if n < 2:
        return n
    return f(n - 2) + f(n - 1)


print(f(2))