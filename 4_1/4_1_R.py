def merge(a, b):
    t = list(a + b)
    ans = []
    while len(t) != 0:
        ans.append(t.pop(t.index(min(t))))

    return tuple(ans)

result = merge((1, 2), (3, 4, 5))
print(result)