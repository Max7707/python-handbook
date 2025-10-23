def split_numbers(text):
    ans = []
    for i in text.split():
        ans.append(i)
    return tuple(ans)


result = split_numbers("1 2 3 4 5")
print(result)