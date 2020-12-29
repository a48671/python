# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, title):

        self.title = title

    def draw(self):

        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):

    def draw(self):

        print(f'Запуск отрисовки ручки с именем {self.title}')


class Pencil(Stationery):

    def draw(self):

        print(f'Запуск отрисовки карандаша с именем {self.title}')


class Handle(Stationery):

    def draw(self):

        print(f'Запуск отрисовки маркера с именем {self.title}')


pen = Pen('волшебная ручка')
pencil = Pencil('мягкий карандаш')
handle = Handle('маркер строительный')

pen.draw()
pencil.draw()
handle.draw()
