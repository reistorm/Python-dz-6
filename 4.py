# Для натурального n создать словарь 
# индекс-значение, состоящий из элементов 
# последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

data = '1 2 3 4 5 6'.split()
result = map(int, data)
my_list = list(map(lambda x: (3*x+1), result))
print(my_list)
numbers = [i for i in range(1, 7)]

d = list(zip(numbers, my_list))
print(d)

# Вопрос: как можно в выводе разделители сделать как ":" ?