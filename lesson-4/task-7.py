# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
#     Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
#     начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from math import factorial

def fact(n):
    state = 1
    for item in range(1, n+1):
        state *= item
        yield state

fact1 = fact(5)

for el in fact(5):
    print(el)

print('test: ', factorial(5))

# Это я так, чтобы поаробовать функцию next
fact_test = fact(3)
print(next(fact_test))
print(next(fact_test))
print(next(fact_test))

