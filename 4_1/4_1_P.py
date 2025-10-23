def is_palindrome(x):
    if isinstance(x, int):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
    elif x == x[::-1]:
        return True
    else:
        return False
    
result = is_palindrome([1, 2, 1, 2, 1])
print(result)