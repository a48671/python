def sum_without_lower(a, b, c):
    sort_by_high = [a, b, c]
    sort_by_high.sort(reverse=True)
    return sort_by_high[0] + sort_by_high[1]

test_1 = sum_without_lower(1, 2, 3) # 5
test_2 = sum_without_lower(11, 20, 3) # 31
test_3 = sum_without_lower(100, 2, 3) # 103
test_4 = sum_without_lower(0, 3, 0) # 3

# test
if test_1 == 5 and test_2 == 31 and test_3 == 103 and test_4 == 3:
    print('ok')
else:
    print('test error')