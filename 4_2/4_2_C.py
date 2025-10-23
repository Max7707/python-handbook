def gcd(*numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        curr_gcd = numbers[0]
        for i in range(1, len(numbers)):
            a = curr_gcd
            b = numbers[i]
            while a != 0 and b != 0:
                if a > b:
                    a = a % b
                elif a <= b:
                    b = b % a
            curr_gcd = a + b
        return curr_gcd

result = gcd(3)
print(result)