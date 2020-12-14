my_list = [7, 5, 3, 3, 2]

numeric = int(input('Input numeric\n'))

index = len(my_list) - 1

while index >= 0:

    current = my_list[index]

    if numeric < current or numeric == current:
        my_list.insert(index + 1, numeric)
        break
    elif index == 0:
        my_list.insert(0, numeric,)

    index -= 1

print(my_list)