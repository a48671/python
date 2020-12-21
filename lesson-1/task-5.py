income = float(input('What is the income of your company?'))
consumption = float(input('What is the consumption of your company?'))

result = 'profit'

if income < consumption:
    result = 'loss'

print(f'Your company received {result}')

if result == 'profit':

    print(f'Profitability your company is {income / (income - consumption)}')

    workers_quantity = int(input('How many workers does your company have?'))

    print(f'Every worker earned {(income - consumption) / workers_quantity}')
