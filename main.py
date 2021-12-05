from abc import ABC, abstractmethod
#1
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        print("Матрица инициализирована")

    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range (len(self.matrix[0]))] for i in range(len(other.matrix))]
        return Matrix(result)

    def __str__(self):
        print("Начало матрицы")
        for i in self.matrix:
            print(i)
        print("Конец матрицы")
matrix = Matrix([[1,2, 3], [2, 1, 5], [2, 1, 5], [2, 1, 5]])
matrix2 = Matrix([[1, 2, 3], [2, 1, 5], [2, 1, 5], [2, 1, 5]])

matrix3 = matrix.__add__(matrix2)

matrix.__str__()
matrix3.__str__()

#2
class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def tissue_consumption(self):
        pass



class Coat(Clothes):
    def __init__(self, title, V):
        self.title = title
        self.V = V

    def tissue_consumption(self):
        return round(self.V/6.5 + 0.5, 4)

    @property
    def costume_property(self):
        return f"Параметры, переданные в класс:" \
               f" {self.title}, {self.V}"

class Costume(Clothes):
    def __init__(self, title, H):
        self.title = title
        self.H = H

    def tissue_consumption(self):
        return round(2 * self.H + 0.3, 4)

    @property
    def costume_property(self):
        return f"Параметры, переданные в класс:" \
               f" {self.title}, {self.H}"


coat = Coat("Пальто 1", 58)
print(coat.tissue_consumption(), "расход ткани")

costume = Costume("Костьюм 1", 5)
print(coat.tissue_consumption(), "расход ткани")
print(costume.tissue_consumption(), "расход ткани")
print(coat.costume_property)
print(costume.costume_property)

class Cell:
    def __init__(self, count):
        self.cell_count = count

    def __add__(self, other):
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        return Cell(self.cell_count - other.cell_count if self.cell_count - other.cell_count > 0 else  "Клеток меньше 0")
    def __mul__(self, other):
        return Cell(self.cell_count * other.cell_count)
    def __truediv__(self, other):
        return Cell(self.cell_count // other.cell_count if self.cell_count // other.cell_count > 0 else "Клеток меньше 0")

    def make_order(self, num: int):
        str = ""
        count = self.cell_count // num
        for i in range(num):
            for j in range(count):
                str = str + "*"
            str = str + "\n"
        return str

cell_1 = Cell(30)
cell_2 = Cell(8)
cell_3 = cell_1.__sub__(cell_2)
print(cell_3.cell_count)
print(cell_3.make_order(5))