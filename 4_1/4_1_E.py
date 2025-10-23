def click():
    global count
    count += 1
    return count

def get_count():
    return count

count = 0
click()
click()
click()
print(get_count())