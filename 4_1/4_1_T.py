def the_roman_ss(n):
    ss = ["I", "V", "X", "L", "C", "D", "M"]

    r_number = ""
    digit = 0
    while n != 0:
        s = str(n % 10)
        n //= 10
        if s in "123":
            r_number += ss[digit] * int(s)
        if s in "4":
            r_number += ss[digit + 1] + ss[digit]
        if s in "5":
            r_number += ss[digit + 1]
        if s in "678":
            r_number += ss[digit] * (int(s) - 5) + ss[digit + 1]
        if s in "9":
            r_number += ss[digit + 2] + ss[digit]
        
        digit += 2

    return r_number[::-1]


def roman(a, b):
    return f"{the_roman_ss(a)} + {the_roman_ss(b)} = {the_roman_ss(a + b)}"


result = roman(1499, 2500)
print(result)