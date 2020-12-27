# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


from utils.utils import get_target_file_path

eng = []

rus = []

keys = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open(get_target_file_path(__file__, 'task-4.txt'), 'r') as f_obj:

    with open(get_target_file_path(__file__, 'task-rus-4.txt'), 'w') as f_obj_rus:

        for line in f_obj.readlines():

            words = line.split()

            words[0] = keys[words[0]]

            f_obj_rus.writelines(' '.join(words) + '\n')
