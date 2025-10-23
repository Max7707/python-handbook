def find_mountains(data):

    rows = len(data)
    columns = len(data[0])
    mountains = []

    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            curr = data[i][j]
            table = [
                data[i - 1][j - 1], data[i - 1][j], data[i - 1][j + 1],
                data[i][j - 1], data[i][j + 1], 
                data[i + 1][j - 1], data[i + 1][j], data[i + 1][j + 1]
            ]
            if all(curr > neighbour for neighbour in table):
                mountains.append((i + 1, j + 1))
    return tuple(mountains)

result = find_mountains([
    [1, 1, 1, 1, 1, 1],
    [1, 2, 1, 5, 4, 1],
    [1, 1, 1, 3, 4, 3],
    [2, 3, 3, 1, 2, 3],
    [1, 2, 1, 3, 2, 1]
])
print(result)