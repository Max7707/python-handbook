def recursive_digit_sum(n):
    if n == 0:
        return n
    else:
        return (n % 10) + recursive_digit_sum(n // 10)
    

result = recursive_digit_sum(7321346)
print(result)