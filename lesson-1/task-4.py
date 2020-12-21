number = int(input('Input number, pleas'))

max_number = 0

denominator = 1

while number != number % denominator:

    current_number = number % (denominator * 10) // denominator

    print('current_number ', current_number)

    if current_number > max_number:
        max_number = current_number

    denominator *= 10

print(f'Max numeric in number {number} is {max_number}')