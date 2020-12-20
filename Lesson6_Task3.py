class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return (f"{self.name} {self.surname}")

    def get_total_income(self):
        return (self._income["wage"] + self._income["bonus"])


cWorker1 = Position("Иван", "Иванов", "Директор", {"wage": 10, "bonus": 5})
print(cWorker1.get_full_name())
print(cWorker1.get_total_income())
