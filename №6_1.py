from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'желтый', 'зеленый']

    def running(self):
        while True:
            print(f'Цвет светофора: {self.__color[0]}')
            sleep(7)
            print(f'Цвет светофора: {self.__color[1]}')
            sleep(2)
            print(f'Цвет светофора: {self.__color[2]}')
            sleep(7)
            print(f'Цвет светофора: {self.__color[1]}')
            sleep(2)


Traffic = TrafficLight()
Traffic.running()
