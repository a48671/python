# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


from utils.utils import get_target_file_path

with open(get_target_file_path(__file__, 'task-2.txt'), 'r') as f_obj:

    content = f_obj.readlines()

    print(f'In file {len(content)} lines')

    for index, line in enumerate(content):

        words_count = len(line.split(' '))

        print(f'In {index + 1} line - {words_count} words')
