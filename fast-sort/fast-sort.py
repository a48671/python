def fast_sort(array):
    if len(array) < 2:
        return array
    medium_index = len(array)//2
    medium = array[medium_index]
    less = [item for index, item in enumerate(array) if index != medium_index and item <= medium]
    larger = [item for index, item in enumerate(array) if index != medium_index and item > medium]
    return fast_sort(less) + [medium] + fast_sort(larger)

my_list = [1, 3, 5, 3, 2, 1, 8, 4, 6, 7, 10, 11, 43, 56, 0]
sorted_list = fast_sort(my_list);

print('test length:', len(my_list) == len(sorted_list))
print('result: ', sorted_list)

