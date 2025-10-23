alphabet = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''}


with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
    with open("cirillic.txt", encoding="UTF-8") as file_in:
        ans = ""
        for line in file_in:
            for sym in line:
                if sym.upper() in alphabet:
                    if sym.isupper():
                        ans += alphabet[sym.upper()].capitalize()
                    else:
                        ans += alphabet[sym.upper()].lower()
                else:
                    ans += sym
    print(ans, file=file_out)