# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle

def get_numbers(start, end):
    result = []
    for item in count(start, 1):
        if item > end:
            break
        result.append(item)
    return result

print(get_numbers(10, 30))

def repeater(array, quantity):
    n = 0
    for item in cycle(array):
        if n / len(array) >= quantity:
            break
        print(item, end=' ')
        n += 1

repeater(['H', 'e', 'l', 'l', 'o'], 3)