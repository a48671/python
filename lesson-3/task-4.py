def my_func(a, b):
    if b < 0 and a == 0:
        return None
    return a ** b

test_0 = my_func(3, 6) # 729
test_1 = my_func(2, -5) # 0.03125
test_2 = my_func(0, -5) # None

# test my_func
if test_0 == 729 and test_1 == 0.03125 and test_2 is None:
    print('my_func ok')
else:
    print('test my_func error')

def my_function(a, b):
    if b < 0 and a == 0:
        return None
    result = a
    for item in range(abs(b) - 1):
        result *= a
    if b < 0:
        return 1/result
    return result

test_3 = my_function(2, -5) # 0.03125
test_4 = my_function(0, -5) # None
test_5 = my_function(3, 6) # 729

# test my_function
if test_3 == 0.03125 and test_4 is None and test_5 == 729:
    print('my_function ok')
else:
    print('test my_function error')