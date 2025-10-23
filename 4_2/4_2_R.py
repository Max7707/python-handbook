print(dict(map(
    lambda item: ("".join(i for i in item[0].lower() if i.isalpha()),
                sum(item[1]) if hasattr(item[1], "__iter__")
                and not isinstance(item[1], (str, dict)) else item[1]),
    {'First 1': 2, 'second:': (2, 1, 1), 'THIRD': [1, 2, 3]}.items()
)))