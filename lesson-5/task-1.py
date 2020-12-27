# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

from utils.utils import get_target_file_path

with open(get_target_file_path(__file__, 'task-1.txt'), 'w') as f_obj:

    str_list = []

    while True:

        string = input('Input text: ')

        if string == '':
            break

        str_list.append(string)

    for index, item in enumerate(str_list):

        f_obj.writelines(item + '\n')
