# Найти сумму чисел 
# списка стоящих на нечетной позиции

def sum_odd(my_list):
    sum = 0
    for i in range(len(my_list)):
        if i % 2 != 0:
            sum += my_list[i]
    return sum
my_list = [i for i in range(1, 15) if i % 2 != 0]
print(my_list)
result = sum_odd(my_list)
print(sum_odd(my_list))

