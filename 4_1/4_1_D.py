def take_small(money):
    new_money = []
    for i in money:
        if i < 100:
            new_money.append(i)
    print(new_money)

money = [1, 5, 200, 0.5, 0.05, 10, 25, 1000, 5000, 1, 2, 100, 0.1, 5, 2000, 0.01]
result = take_small(money)