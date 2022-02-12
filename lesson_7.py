#Задание 1
# class Matrix:
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __str__(self):
#         txt_m: str = "";
#
#         for i in range(0, len(self.matrix)):
#             for j in range(0, len(self.matrix[i])):
#                 txt_m += "%3d" % (self.matrix[i][j])
#
#                 if j != len(self.matrix[i]) - 1:
#                     txt_m += " ";
#
#             if i != len(self.matrix) - 1:
#                 txt_m += "\n"
#
#         return txt_m
#
#     def __add__(self, other):
#         new_matrix: list = []
#
#         for i in range(0, len(self.matrix)):
#             line: list = []
#
#             for j in range(0, len(self.matrix[i])):
#                 line.append(self.matrix[i][j] + other.matrix[i][j])
#
#             new_matrix.append(line)
#
#         return Matrix(new_matrix)
#
#
# m1: Matrix = Matrix([[1, 2, 3, 0], [4, 5, 6, 0], [7, 8, 9, 0]])
# m2: Matrix = Matrix([[1, 2, 3, 0], [4, 5, 6, 0], [7, 8, 9, 0]])
# print(m1)
# print("----------------")
# print(m2)
# print("----------------")
# print(m1 + m2)

#Задание 2
# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#     @abstractmethod
#     def costs(self):
#         pass
#
#
# class Coat(Clothes):
#     def __init__(self, v: float):
#         self.v = v
#         self.cost = v
#
#     @property
#     def cost(self):
#         return self.__cost
#
#     @cost.setter
#     def cost(self, cost):
#         self.__cost = cost / 6.5 + 0.5
#
#     def costs(self):
#         return self.cost
#
#
# class Suit(Clothes):
#     def __init__(self, h: float):
#         self.h = h
#
#     def costs(self):
#         return 2 * self.h + 0.3
#
# c: Coat = Coat(13)
# print(c.costs())
#
# s: Suit = Suit(2)
# print(s.costs())

#Задание 3
# class Cell:
#     def __init__(self, cell: int):
#         self.cell = cell
#
#     def __add__(self, other):
#         return Cell(self.cell + other.cell)
#
#     def __sub__(self, other):
#         if self.cell - other.cell < 0:
#             print("Поменяйте операнды местами")
#             return None
# 
#         return Cell(self.cell - other.cell)
#
#     def __mul__(self, other):
#         return Cell(self.cell * other.cell)
#
#     def __truediv__(self, other):
#         return Cell(round(self.cell / other.cell))
#
#     def __str__(self):
#         return str(self.cell)
#
#     def make_order(other, len):
#         txt: str = ""
#
#         for i in range(1, other.cell + 1):
#             txt += "*"
#             if i % len == 0 and other.cell != i:
#                 txt += "\n"
#
#         return txt
#
#
# c1: Cell = Cell(10)
# c2: Cell = Cell(13)
#
# print(f"c1 + c2 = {c1 + c2}")
# print(f"c1 - c2 = {c1 - c2}")
# print(f"c1 * c2 = {c1 * c2}")
# print(f"c1 / c2 = {c1 / c2}")
#
# print(Cell.make_order(Cell(12), 5))