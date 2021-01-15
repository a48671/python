# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class ErrorZeroDivisioner(Exception):
    def __init__(self, txt):
        self.txt = txt


def division(num, divisioner):

    try:

        if divisioner == 0:
            raise ErrorZeroDivisioner('Division on 0 forbidden')
        else:
            return num / divisioner

    except ErrorZeroDivisioner as err:
        print(err)
        return None


print(division(4, 2))
print(division(4, 0))
