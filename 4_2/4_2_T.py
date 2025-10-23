import re 
from datetime import datetime

database = []


def insert(*users):
    for user in users:
        database.append(user)
    database.sort(key=lambda x: x["id"])
    return database


def select(*criteria):
    result = list(database)
    if not criteria:
        return result
    
    for i in criteria:
        m = re.match(r"(\w+)\s*(=|>|<|>=|<=|!=|~)\s+(.+)", i)
        if not m:
            continue
        field, op, value = m.groups()

        if field == "id":
            comp_value = int(value)
        elif field == "birth":
            comp_value = datetime.strptime(value, "%d.%m.%Y")
        else:
            comp_value = value

        if op == "=":
            result = [u for u in result if (int(u[field]) if field=="id" else
                                            datetime.strptime(u[field], "%d.%m.%Y") if field=="birth" else
                                            u[field]) == comp_value]
        if op == "!=":
            result = [u for u in result if (int(u[field]) if field=="id" else
                                            datetime.strptime(u[field], "%d.%m.%Y") if field=="birth" else
                                            u[field]) != comp_value]
        if op == ">":
            result = [u for u in result if (int(u[field]) if field=="id" else
                                            datetime.strptime(u[field], "%d.%m.%Y") if field=="birth" else
                                            u[field]) > comp_value]
        if op == "<":
            result = [u for u in result if (int(u[field]) if field=="id" else
                                            datetime.strptime(u[field], "%d.%m.%Y") if field=="birth" else
                                            u[field]) < comp_value]
        if op == ">=":
            result = [u for u in result if (int(u[field]) if field=="id" else
                                            datetime.strptime(u[field], "%d.%m.%Y") if field=="birth" else
                                            u[field]) >= comp_value]
        if op == "<=":
            result = [u for u in result if (int(u[field]) if field=="id" else
                                            datetime.strptime(u[field], "%d.%m.%Y") if field=="birth" else
                                            u[field]) <= comp_value]
        if op == "~":
            result = [u for u in result if re.search(comp_value, str(u[field]))]

    return result


insert({'id': 1, 'name': 'Ann', 'birth': '01.03.2001'})
insert(
    {'id': 3, 'name': 'Bob', 'birth': '05.03.2002'},
    {'id': 4, 'name': 'Chuck', 'birth': '07.06.2001'}
)
print([user['name'] for user in select()])
print([user['name'] for user in select("name > B")])
insert({'id': 2, 'name': 'Den', 'birth': '29.02.2000'})
print([user['name'] for user in select("name > B")])
print([user['name'] for user in select("id <= 2")])
print(*select("birth >= 12.04.2001"), sep="\n")

