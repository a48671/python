# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
from functools import reduce

my_list = list(item for item in range(100, 1001, (1000-100)//(4-1)))

print('my_list: ', my_list)
print('length is: ', len(my_list))

print('result: ', reduce(lambda a, b: a*b, my_list))