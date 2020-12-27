# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from utils.utils import get_target_file_path

with open(get_target_file_path(__file__, 'task-5.txt'), 'w') as f_obj:

    f_obj.write(' '.join([str(item) for item in range(1, 30, 2)]))

with open(get_target_file_path(__file__, 'task-5.txt'), 'r') as f_obj_red:

    total = sum(map(lambda item: int(item), f_obj_red.read().split()))

print(total)
