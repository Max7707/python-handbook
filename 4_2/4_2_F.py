def get_operator(n):
    if n == "+":
        return lambda a, b: a + b
    if n == "-":
        return lambda a, b: a - b
    if n == "*":
        return lambda a, b: a * b
    if n == "//":
        return lambda a, b: a // b
    if n == "**":
        return lambda a, b: a ** b
    
operator_power = get_operator("**")
print(operator_power(2, 10))