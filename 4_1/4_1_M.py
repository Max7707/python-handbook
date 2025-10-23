early_text = []


def modern_print(text):
    global early_text
    if text in early_text:
        None
    else:
        early_text.append(text)
        print(text)


modern_print("Ало!")
modern_print("Ало!")
modern_print("Я тебя не слышу")
modern_print("Ало!")
modern_print("Ало!")
modern_print("Позвони когда сможешь")
modern_print("Позвони когда сможешь")
modern_print("Я тебя не слышу")