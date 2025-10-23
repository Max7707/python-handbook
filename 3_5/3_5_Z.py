p=0
with open("sample01 (2).num", "rb") as file:
    while i := file.read(2):
        n = int.from_bytes(i)
        p+=n
print(bytes([p % 2**16]))
# print(hex(p % 2**16))      