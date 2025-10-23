def make_matrix(size, value=0):
    if isinstance(size, tuple):
        n, m = size
    else:
        n = m = size
    ans = []
    for i in range(m):
        curr = []
        for j in range(n):
            curr.append(value)
        ans.append(curr)

    return ans


result = make_matrix((4, 2), 1)
print(result)