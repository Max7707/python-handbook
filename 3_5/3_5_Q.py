file = input()

ans = ""
with open(file, encoding="UTF-8") as file_in:
    for symbol in file_in.read():
        
        if ord(symbol) > 128:
            ans += chr(ord(symbol) % 256)
        else:
            ans += chr(ord(symbol)) 
print(ans)