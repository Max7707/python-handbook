def only_positive_even_sum(a, b):
    if isinstance(a, int) or isinstance(b, int):
        if (a > 0 and a % 2 == 0) and (b > 0 and b % 2 == 0):
            return a + b
        else:
            raise ValueError
    else:
        raise TypeError
    

print(only_positive_even_sum(-5, 4))