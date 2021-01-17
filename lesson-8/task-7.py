# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:

    a = 0
    b = 0

    def __init__(self, a: object, b: object) -> object:
        if type(a) == int or float and type(b) == int or float:
            self.a = a
            self.b = b
        else:
            print('input arguments invalid')


    def __str__(self):
        operator = '+'
        if self.b < 0:
            operator = ''
        return f'{self.a}{operator}{self.b}i'

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.a + other.a, self.b + other.b)
        else:
            print('not a complex number')
            return None

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            a = (self.a * other.a) + (self.b * other.b) * -1
            b = self.b * other.a + self.a * other.b
            return ComplexNumber(a, b)
        else:
            print('not a complex number')
            return None


z1 = ComplexNumber(1, 3)
z2 = ComplexNumber(4, -5)
z3 = ComplexNumber(8, 'ada')
z4 = ComplexNumber(1, -1)
z5 = ComplexNumber(3, 6)

print('z1 = ', z1)
print('z2 = ', z2)
print('z1 + z2 = ', z1 + z2)
print('z1 + "sd" = ', z1 + 'sd')
print('z4 * z5 = ', z4 * z5)
