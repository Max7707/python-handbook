def fragments(numbers):
    ans = []
    curr = []
    for number in numbers:
        if not curr or number > curr[-1]:
            curr.append(number)
        else:
            ans.append(curr)
            curr = [number]
    if curr:
        ans.append(curr)
    return(ans)

result = fragments([0, 4, 5, -9, -6, 3, 2, 3, 4, 9])
print(result)
        
