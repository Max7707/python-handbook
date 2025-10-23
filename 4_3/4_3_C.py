def make_equation(*coefficients):
    if len(coefficients) == 1:
        return str(coefficients[0])
    else:
        return f"({make_equation(*coefficients[:-1])}) * x + {coefficients[-1]}"

result = make_equation(3, 2, 1)
print(result) 
