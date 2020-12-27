# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


from utils.utils import get_target_file_path

workers = {}

with open(get_target_file_path(__file__, 'task-3.txt'), 'r') as f_obj:

    for line in f_obj.readlines():

        key, value = line.split()

        workers[key] = int(value)

less_20 = [key for key in workers if workers[key] < 20000]

print(f'less 20000 {less_20}')

medium = sum(map(lambda key_worker: workers[key_worker], workers))/len(workers)

print(f'medium {medium}')