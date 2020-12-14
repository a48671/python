text_message = '\n'.join([
    'Введите эллементы списка, через запятую',
    'Нвпример: первый_элемент, второй_элемент, третий_элемент',
    'После запятой, обязательно должен следовать один пробел',
    ''
])

new_list = input(text_message).split(', ');

index = 0

while index < len(new_list):

    print(index)

    if index % 2 != 0:
        current_item = new_list[index]

        new_list[index] = new_list[index - 1]
        new_list[index - 1] = current_item

    index += 1

print(new_list)