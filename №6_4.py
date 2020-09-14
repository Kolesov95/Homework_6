class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} становилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def showspeed(self):
        print(f'{self.name} едет со скоростью {self.speed}')


class TownCar(Car):
    def showspeed(self):
        super().showspeed()
        print('Вы превышаете скорость!' if self.speed > 60 else None)


class SportCar(Car):
    def go(self):
        print(f'{self.name} поехала. Внимание: аккуратнее на дорогах')


class WorkCar(Car):
    def showspeed(self):
        super().showspeed()
        print('Вы превышаете скорость!' if self.speed > 40 else None)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


car_1 = TownCar(100, 'красный', 'Ауди', False)
car_2 = SportCar(140, 'синий', 'Ферарри', False)
car_3 = WorkCar(35, 'желтый', 'Трактор', False)
car_4 = PoliceCar(70, 'синий', 'Тайота')

print(car_1.speed, car_1.color, car_1.name, car_1.is_police)
print(car_2.speed, car_2.color, car_2.name, car_2.is_police)
print(car_3.speed, car_3.color, car_3.name, car_3.is_police)
print(car_4.speed, car_4.color, car_4.name, car_4.is_police)
car_1.go()
car_2.go()
car_1.showspeed()
car_4.turn('на лево')
car_4.stop()
