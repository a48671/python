# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула(куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    speed = 0

    def __init__(self, color, name, is_police):

        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):

        self.speed = speed

        print(f'Машина {self.name} поехала')

    def stop(self):

        print(f'Машина {self.name} остановилась')

    def turn(self, direction):

        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):

        if self.speed:

            print(f'Машина {self.name} едет со скоростью {self.speed} км/ч')

        else:

            print(f'Машина {self.name} стоит на месте')


class TownCar(Car):

    def show_speed(self):

        super().show_speed()

        if self.speed > 60:

            print(f'Скорость машины {self.name} превышена')


class SportCar(Car):

    pass


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()

        if self.speed > 40:

            print(f'Скорость машины {self.name} превышена')


class PoliceCar(Car):

    pass


police = PoliceCar(color='Red', name='PoliceCar', is_police=True)
my_car = TownCar(color='White', name='TownCar', is_police=False)
taxi = WorkCar(color='Yellow', name='WorkCar', is_police=False)
sport = SportCar(color='Blue', name='SportCar', is_police=False)

police.show_speed()
police.go(60)
police.show_speed()
police.turn('налево')

print('\n')

my_car.show_speed()
my_car.go(80)
my_car.show_speed()
my_car.turn('направо')

print('\n')

taxi.show_speed()
taxi.go(40)
taxi.show_speed()
taxi.turn('направо')

print('\n')

taxi.show_speed()
taxi.go(50)
taxi.show_speed()
taxi.turn('налево')

print('\n')

sport.show_speed()
sport.go(150)
sport.show_speed()
sport.turn('на 180 градусов')
