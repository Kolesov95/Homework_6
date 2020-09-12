class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход сотрудника {self.name} {self.surname}: {sum(self._income.values())}'


worker_1 = Position('Иван', 'Иванов', 'Разработчик', 50000, 20000)
worker_2 = Position('Петр', 'Петров', 'Бухгалтер', 45000, 15000)

print(worker_1.get_full_name())
print(worker_2.get_total_income())
