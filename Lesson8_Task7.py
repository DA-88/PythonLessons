class Complex:
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im

    def __add__(self, other):
        m = Complex(self.Re + other.Re, self.Im + other.Im)
        return m

    def __sub__(self, other):
        m = Complex(self.Re - other.Re, self.Im - other.Im)
        return m

    def __mul__(self, other):
        a = self.Re
        b = self.Im
        c = other.Re
        d = other.Im
        m = Complex(a * c - b * d, b * c + a * d)
        return m


a = Complex(2, 3)
b = Complex(4, 5)
a = a * b
print(a.Re, a.Im)
