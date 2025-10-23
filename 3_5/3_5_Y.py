n = int(input()) % 26

ans = ""
with open("public.txt", encoding="UTF-8") as file:
    for i in file.read().strip("\n"):
        if i.isalpha():
            s = ord(i)
            if n == 0:
                ans += chr(s)
            if i.isupper():
                if (s + n) in range(65, 91):
                    ans += chr(s + n)
                else:
                    if n > 0:
                        ans += chr(s + n - 26)
                    if n < 0:
                        ans += chr(s + n + 26)
            if i.islower():
                if (s + n) in range(97, 123):
                    ans += chr(s + n)
                else:
                    if n > 0:
                        ans += chr(s + n - 26)
                    if n < 0:
                        ans += chr(s + n + 26)
        else:
            ans += i

with open("private.txt", "w", encoding="UTF-8") as file_out:
    n = file_out.write(ans)