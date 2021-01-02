import datetime


class Sklad:
    def __init__(self, capacity: int):
        self.storage = [0] * capacity
        self.total_capacity = capacity
        self.free_capacity = capacity
        self.log = []

    def PutItem(self, item):
        i: int
        if self.free_capacity > 0:
            i = 0
            while i <= len(self.storage) - 1:
                if self.storage[i] == 0:
                    self.storage[i] = item
                    self.free_capacity -= 1
                    now = datetime.datetime.now()
                    s = now.strftime("%d-%m-%Y %H:%M:%S")
                    self.log.append(
                        f"{s} поступил на склад: {item.org_type}, вес - {item.weight}, возраст - {item.age}")
                    break
                i += 1
        else:
            print("Склад уже заполнен")
            return "Склад уже заполнен"

    def ListItem(self):
        i: int
        i = 1
        for el in self.storage:
            if el != 0:
                print(f"{i} - {el.org_type}, вес - {el.weight}, возраст - {el.age}")
            i += 1
        print(f"Свободных мест {self.free_capacity} из {self.total_capacity}")

    def RemoveItem(self, position: int, destination: str):
        if position > 0 and position <= self.total_capacity:
            position -= 1
            if self.storage[position] != 0:
                now = datetime.datetime.now()
                s = now.strftime("%d-%m-%Y %H:%M:%S")
                self.log.append(
                    f"{s} отправлен со склада в {destination}: {self.storage[position].org_type}, вес - {self.storage[position].weight}, возраст - {self.storage[position].age}")
                self.storage.pop(position)
                self.storage.append(0)
                self.free_capacity += 1
        else:
            print("Неверно указана позиция склада")

    def PrintLog(self):
        for el in self.log: print(el)


class Org:
    def __init__(self, org_type: str, weight: int):
        self.org_type = org_type
        self.weight = weight


class Printer(Org):
    def __init__(self, weight: int, age: int):
        self.org_type = "Printer"
        self.weight = weight
        self.age = age


class Computer(Org):
    def __init__(self, weight: int, age: int):
        self.org_type = "Computer"
        self.weight = weight
        self.age = age


s = Sklad(10)
s.PutItem(Printer(3, 5))
s.PutItem(Printer(3, 5))
s.PutItem(Computer(3, 5))
s.ListItem()
s.PrintLog()
s.RemoveItem(2, "Бухгалтерия")
s.ListItem()
s.PrintLog()
