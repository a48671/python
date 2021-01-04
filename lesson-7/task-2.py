# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class Clothes:

    def __init__(self, type_clothes, size):

        self.type = type_clothes

        if self.type == 'coat':

            self.v = size

        else:

            self.h = size

    def __str__(self):

        return self.type

    @property
    def get_consumption(self):

        if self.type == 'coat':

            return self.v / 6.5 + 0.5

        else:

            return 2 * self.h + 0.3


coat = Clothes(type_clothes='coat', size=48)
costume = Clothes(type_clothes='costume', size=1.7)

print(f'consumption for coat: {coat.get_consumption}')
print(f'consumption for costume: {costume.get_consumption}')
