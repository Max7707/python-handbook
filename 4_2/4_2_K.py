def order(*drinks):
    ingredients = {
        "Эспрессо": {"coffee": 1}, "Капучино": {"coffee": 1, "milk": 3},
        "Макиато": {"coffee": 2, "milk": 1}, "Кофе по-венски": {"coffee": 1, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1}, 
        "Кон Панна": {"coffee": 1, "cream": 1}
                  }
    
    for drink in drinks:
        if all(ingredients[drink][i] <= in_stock[i] for i in ingredients[drink]):
            for j in ingredients[drink]:
                in_stock[j] = in_stock[j] - ingredients[drink][j]
            return drink
    return "К сожалению, не можем предложить Вам напиток"



in_stock = {"coffee": 4, "milk": 4, "cream": 0}
print(order("Капучино", "Макиато", "Эспрессо"))
print(in_stock)
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))