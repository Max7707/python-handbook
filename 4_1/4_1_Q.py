def is_prime(n):
    if n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True
    
result = is_prime(1)
print(result)