import time


class TrafficLight:
    def __init__(self):
        self.color = "red"

    def running(self):
        if self.color == "red":
            time.sleep(7)
            self.color = "yellow"
            return (None)
        if self.color == "yellow":
            time.sleep(2)
            self.color = "green"
            return (None)
        if self.color == "green":
            time.sleep(5)
            self.color = "red"
            return (None)


i = 0
cTrafficLight = TrafficLight()
while i <= 50:
    print(cTrafficLight.color)
    cTrafficLight.running()
    i += 1
