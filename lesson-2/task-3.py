season_list = ['', 'w', 'w', 'sp', 'sp', 'sp', 'sum', 'sum', 'sum', 'a', 'a', 'a', 'w']

seasons = {
    'w': 'Winter',
    'sp': 'Spring',
    'sum': 'Summer',
    'a': 'Autumn'
}

month_number = int(input('Input month number\n'))

while month_number > 12 or month_number < 1:
    month_number = int(input('Month number should be number from 1 to 12\n'))

print(seasons[season_list[month_number]])