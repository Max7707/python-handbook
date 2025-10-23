def max2D(matrix):
    ans = []
    for m in matrix:
        ans.extend(m)
    return max(ans)


result = max2D([[-5, -43, 72, 89], [-40, 92, -1, -73], [30, -75, 23, 94]])
print(result)