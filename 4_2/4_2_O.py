def get_repeater(func, count):
    def repeater(x):
        result = x
        for i in range(count):
            result = func(result)
        return result
    return repeater


repeater = get_repeater(lambda x: x + 1, 5)
print(repeater(2))