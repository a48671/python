my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print([item for item in my_list if len(list(filter(lambda x: x == item, my_list))) == 1])