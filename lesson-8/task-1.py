# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:

    date_string = 'sd'
    day = 0
    month = 0
    year = 0

    def __init__(self, date_string):
        Date.date_string = date_string

    @classmethod
    def get_day(cls):
        print('date_string: ', cls.date_string)
        return cls.date_string.split('-')[0]

    @classmethod
    def get_month(cls):

        return cls.date_string.split('-')[1]

    @classmethod
    def get_year(cls):

        return cls.date_string.split('-')[2]


    @staticmethod
    def validate_date(date):

        invalid = False

        for index, item in enumerate(date.split('-')):

            if item.isdigit() and index == 0 and (int(item) > 31 or int(item) == 0):
                print('day invalid')
                invalid = True
            elif item.isdigit() and index == 1 and (int(item) > 12 or int(item) == 0):
                print('month invalid')
                invalid = True
            elif not item.isdigit() and index == 2:
                print('year invalid')
                invalid = True

        if invalid:

            return False

        print('date is valid')

        return True


date = Date('11-11-2009')

print('day: ', date.get_day())
print('month: ', date.get_month())
print('year: ', date.get_year())

print('11-11-2009', Date.validate_date('11-11-2009'))
print('11-13-2009', Date.validate_date('11-13-2009'))
print('45-12-2009', Date.validate_date('45-12-2009'))
print('10-12-qwe', Date.validate_date('10-12-qwe'))
