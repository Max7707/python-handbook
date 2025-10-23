def can_eat(horse, other):
    one = abs(horse[0] - other[0])
    two = abs(horse[1] - other[1])
    if (one, two) == (1, 2) or (one, two) == (2, 1):
        return True
    else:
        return False


result = can_eat((5, 5), (6, 6))
print(result)