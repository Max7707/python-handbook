def parse_value(value):
    # int
    if value.isdigit():
        return int(value)
    if value[0] == "-" and value[1:].isdigit():
        return -int(value[1:])
    
    # float
    try:
        return float(value)
    except Exception:
        return value


def get_dict(text):
    t = []
    t += text.split(";")
    ans = dict()
    for i in t:
        key, value = i.split("=")
        ans[key] = parse_value(value)
    return ans


result = get_dict('a=A;b=2;c=-3.5')
print(result)