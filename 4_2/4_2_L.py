data1 = ()
data2 = ()

def enter_results(*args):
    global data1, data2

    data1 += args[::2]
    data2 += args[1::2]
    return data1, data2


def get_sum():
    return (round(sum(data1), 2), round(sum(data2), 2))


def get_average():
    return (round(sum(data1) / len(data1), 2), round(sum(data2) / len(data2), 2))


enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())
enter_results(5.2, 7.3)
print(get_sum(), get_average())
enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
print(get_sum(), get_average())