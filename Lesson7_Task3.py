class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        self.count = self.count + other.count
        return self

    def __sub__(self, other):
        if self.count > other.count:
            self.count = self.count - other.count
        else:
            print("Вычитание невозможно")
        return self

    def __truediv__(self, other):
        self.count = self.count // other.count
        return self

    def __mul__(self, other):
        self.count = self.count * other.count
        return self

    def make_order(self, row_count):
        i = 1
        res = ""
        b = "*" * row_count
        while i <= self.count // row_count:
            res = f"{res}{b}\n"
            i += 1
        b = "*" * (self.count % row_count)
        res = f"{res}{b}"
        return res


m = Cell(12) * Cell(5) + Cell(256) - Cell(300) / Cell(17)
print(m.make_order(42))
