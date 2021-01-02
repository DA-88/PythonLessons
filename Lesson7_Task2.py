class Clothes:
    def __init__(self, type):
        self.type = type


class Coat(Clothes):
    def __init__(self, size):
        self.type = "Coat"
        self.size = size

    @property
    def Tissue_Consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        self.type = "Costume"
        self.height = height

    @property
    def Tissue_Consumption(self):
        return self.height * 2 + 0.3


c = Coat(32)
d = Costume(175)
print(c.Tissue_Consumption)
print(d.Tissue_Consumption)
