my_list = input('Input text\n').split(' ');

index = 0
for letter in my_list:

    print(f'{index} - {letter[0:10]}')

    index += 1