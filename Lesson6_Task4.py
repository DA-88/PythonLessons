class Car:
    def __init__(self, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = "Forward"

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        self.direction = direction

    def show_speed(self):
        print(self.show_speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость превышена! {self.speed}")
        else:
            print(self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость превышена! {self.speed}")
        else:
            print(self.speed)


cTownCar = TownCar("red", "Ivan", False)
cWorkCar = WorkCar("yellow", "Petr", False)
cTownCar.go(61)
cTownCar.show_speed()
cWorkCar.go(41)
cWorkCar.show_speed()
