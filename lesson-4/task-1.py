from sys import argv

def get_salary(duration, value):
    return duration*value

if len(argv) == 3:
    file_name, duration, value = argv
    print(f'salary = {get_salary(int(duration), int(value))}')
else:
    print('not arguments')

