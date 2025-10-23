def find_mountains(heights):
    ans = []
    for index, (left, middle, right) in enumerate(zip(heights, heights[1:], heights[2:]), 2):
        if left < middle > right:
            ans.append(index)
    return tuple(ans)

result = find_mountains([5, 1, 10, 2, 3, 4, 3, 20])
print(result)
  