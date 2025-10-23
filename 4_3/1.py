# Декоратор принимает функцию f как аргумент
def count(f):
    total = 0

    # Объявляем функцию, которая расширяет функционал f
    def decorated(*args, **kwargs):
        # Переменная total объявлена нелокальной для доступа из внутренней функции
        nonlocal total
        total += 1
       # Возвращаем значение исходной функции и дополнительно total
        return f(*args, **kwargs), total
   # Возвращаем новую функцию как объект
    return decorated


@count
def hello(name):
    return f"Hello, {name}"


print(hello("Пользователь_1"))
print(hello("Пользователь_2"))


a = (i + j for i, j in range(10))

print(6 % 3)