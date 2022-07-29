# Дана последовательность чисел. 
# Получить список уникальных элементов 
# заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
list1 = [1,2,3,5,1,5,3,10]
def find_unq_el(in_list1):
    if in_list1 % 2 == 0:
        return True
    else:
        return False

out_filter = filter(find_unq_el, list1)
print(f'Список уникальных элементов', list(out_filter))
