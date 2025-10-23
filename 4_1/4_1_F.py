ans = 0


def move(name, n):
    global ans
    if name == "Петя":
        ans += n
    else:
        ans -= n


def game_over():
    if ans > 0:
        return "Петя"
    if ans < 0:
        return "Ваня"
    if ans == 0:
        return "Ничья"
    

move('Петя', 3)
move('Ваня', 4)
move('Петя', 4)
move('Ваня', 3)
print(game_over())