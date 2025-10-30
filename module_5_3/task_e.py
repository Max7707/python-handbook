from _collections_abc import Iterable


def merge(a, b):
    if not isinstance(a, Iterable) or not isinstance(b, Iterable):
        raise StopIteration

    if len({type(x) for x in (list(a) + list(b))}) != 1:
        raise TypeError

    if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)) or not all(b[i] <= b[i + 1] for i in range(len(b) - 1)):
        raise ValueError

    ans = []
    a_i = 0
    b_i = 0

    while b_i != len(b) and a_i != len(a):
        if b[b_i] <= a[a_i]:
            ans.append(b[b_i])
            b_i += 1
        else:
            ans.append(a[a_i])
            a_i += 1
    
    if b_i == len(b):
        ans.extend(a[a_i:])
    if a_i == len(a):
        ans.extend(b[b_i:])
        
    return ans


print(*merge([3, 2, 1], range(10)))