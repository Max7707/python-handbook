from collections import defaultdict

def secret_replace(text, **args):
    counters = defaultdict(int) # считает, сколько раз мы заменяли каждый символ, создаёт 'a' со значением 0, затем прибавляет 1 
    result = []

    for ch in text:
        if ch in args:
            options = args[ch]
            index = counters[ch] % len(options)
            result.append(options[index])
            counters[ch] += 1
        else:
            result.append(ch)

    return ''.join(result)


result = secret_replace(
    "ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
)
print(result)