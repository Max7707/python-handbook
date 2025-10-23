def product(*args, **named_args):
    ans = tuple()
    for arg in args:
        a = 1
        count_op = 0
        for n in named_args:
            if n in arg:
                a = a * named_args[n]
                count_op += 1
        if count_op != 0:
            ans += (a, )
    return ans

result = product("Ann", "Bob", "Chuck", a=9, n=5, u=3, c=2, A=5)
print(result)