def merge(a, b):
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


def merge_sort(n):
    if len(n) <= 1:
        return n
    else:
        a = merge_sort(n[:len(n) // 2])
        print(a)
        b = merge_sort(n[len(n) // 2:])
        print(b)
        return merge(a, b)


result = merge_sort([3, 1, 5, 3])
print(result)