def choice(*numbers, **kwargs):
    n = list(numbers)
    if "min" in kwargs:
        return min(map(kwargs["min"], n))
    if "max" in kwargs:
        return max(map(kwargs["max"], n))

result = choice(321, 87, 1000, -23, min=lambda x: len(str(x)))
print(result)