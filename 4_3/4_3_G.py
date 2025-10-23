def same_type(f):

    def decorared(*args):
        for i in range(1, len(args)):
            if isinstance(args[i], type(args[i - 1])) is False:
                return f"Обнаружены различные типы данных\n{False}"
        return f(*args)
    
    return decorared
    

@same_type
def combine_text(*words):
    return ' '.join(words)


print(combine_text('Hello,', 'world!') or 'Fail')
print(combine_text(2, '+', 2, '=', 4) or 'Fail')
print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')