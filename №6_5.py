class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки инструментом: {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Вы взяли ручку "{self.title}". Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'Вы взяли карандаш "{self.title}". Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print(f'Вы взяли маркер "{self.title}". Запуск отрисовки маркером')


tool_1 = Pen('Красная')
tool_2 = Pencil('Простой')
tool_3 = Handle('Зеленый')
tool_1.draw()
tool_2.draw()
tool_3.draw()
