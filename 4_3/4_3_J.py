def make_linear(n):
    ans = []
    for i in n:
        if type(i) != list:
            ans.append(i)
        else:
            make_linear(i)      
    return ans


result = make_linear([1, 2, [3]])
print(result)


def make_linear(n):
    ans = []
    for i in n:
        if isinstance(i, list):
            ans.extend(make_linear(i))
        else:
            ans.append(i)
    return ans

result = make_linear([1, 2, [3, 4], 13, [434, 35, [35]], 35])
print(result)