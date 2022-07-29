# Для натурального n создать словарь 
# индекс-значение, состоящий из элементов 
# последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def sq_number(n):
    dict = {}
    if n == 0:
        return 0
    for n in range(1, n+1):
        n = 3 * n + 1
        dict.append(n)
        for v in dict():
            print(v)
sq_number(8)