import itertools


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ""
        for el in self.matrix:
            if result == "":
                result = str(el)
            else:
                result = f"{result}\n{str(el)}"
        return result

    def __add__(self, other):
        self.matrix = [[a + b + d for a, b, d in itertools.zip_longest(x, y, [0] * max(max([len(el) for el in self.matrix]), max([len(el) for el in other.matrix])), fillvalue=0)] for x, y in
                       itertools.zip_longest(self.matrix, other.matrix, fillvalue=[])]
        return self


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
s = Matrix([[10, 20, 30], [40, 50, 60, 70, 80], [7, 8, 9], [17, 19, 29]])
f = Matrix(
    [[0, 0, 0, 0, 0, 100, 100, 100, 100], [0, 0, 0, 0, 0, 100, 100, 100, 100], [0, 0, 0, 0, 0, 100, 100, 100, 100],
     [0, 0, 0, 0, 0, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100, 100, 100],
     [100, 100, 100, 100, 100, 100, 100, 100, 100]])
m = m + s + f + f + m + s
print(m)
