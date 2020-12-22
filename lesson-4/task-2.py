my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([item for index, item in enumerate(my_list) if index > 0 and my_list[index - 1] < item])