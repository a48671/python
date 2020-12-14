my_list = [
    123,
    'string',
    0.123,
    {
        'name': 'Andrey',
        'age': 36
    },
    set('set'),
    ('t', 'u', 'p', 'l', 'e'),
    [1, 2, 3],
    True,
    bytes('Bytes', encoding = 'utf-8'),
    None
]

for item in my_list:
    print(type(item))