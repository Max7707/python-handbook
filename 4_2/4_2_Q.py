print(dict(filter(
    lambda item: isinstance(item[1], list) and any(i % 2 == 0 for i in item[1]),
    {'first': 2, 'second': '2 + 2 = 4', 'third': [1, 2, 3]}.items()
)))