class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def CalcWidth(self, cm_mass, cm):
        return (self._length * self._width * cm_mass * cm)


cRoad = Road(20, 5000)
print(cRoad.CalcWidth(25, 5))
