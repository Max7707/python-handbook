def grow(*args, **named_arg):
    n = list(args)
    ans = tuple()
    for i in n:
        a = i
        for key in named_arg:
            if i % len(key) == 0:
                a = a + named_arg[key]
        ans += (a, )
    return ans


result = grow(12, 5, 30, 60, 15, first=13, second=2, Bob=7)
print(result)