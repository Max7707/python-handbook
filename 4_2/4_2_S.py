def secret_replace(text, **args):
    ans = ""
    for s in text:
        if s in args:
            args[s] = list(args[s])
            n = args[s][0]
            ans += args[s][0]
            args[s].pop(args[s].index(args[s][0])) 
            args[s].append(n)
        else:
            ans += s
    return ans

result = secret_replace(
    "ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
)
print(result)