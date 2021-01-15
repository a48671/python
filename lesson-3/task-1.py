def division(dividend, divider):
    if divider == 0:
        return None
    return dividend / divider

dividend = input('Input dividend: ')
divider = input('Input divider: ')

if dividend.isdigit() and divider.isdigit():
    print(division(int(dividend), int(divider)))
else:
    print('You entered not a number')
