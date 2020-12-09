first_day_result = float(input('Input first day result'))

target_result = float(input('Input target result'))

while target_result < first_day_result:
    target_result = float(input('Target result should be greater first day result. \n Input target result, pleas'))

current_result = first_day_result
current_day = 1

while current_result < target_result:

    current_day += 1
    current_result = current_result + current_result * 0.1

print(f'In {current_day} day sportsmen will reach target result')

