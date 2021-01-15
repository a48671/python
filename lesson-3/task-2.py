def print_user_info(name, surname, patronymic, born, city, email, phone):
    print(f'{name} {surname} {patronymic}, {born}, {city}, {email}, {phone}')

def get_arguments(func):
    arguments = func.__code__.co_varnames
    data = {}
    for item in arguments:
        value = input(f'Input {item}: ')
        data[item] = value
    return data

args = get_arguments(print_user_info)

print_user_info(
    name=args['name'],
    surname=args['surname'],
    patronymic=args['patronymic'],
    born=args['born'],
    city=args['city'],
    email=args['email'],
    phone=args['phone']
)