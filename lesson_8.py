#Задание 1
# class Date:
#     def __init__(self, frm_dt: str):
#         self.frm_dt = frm_dt
#
#     @classmethod
#     def cost_dt_num(cls, dt, flag: str):
#         dt_num: list = dt.frm_dt.split("-")
#
#         if flag == "dd":
#             return int(dt_num[0])
#         elif flag == "mm":
#             return int(dt_num[1])
#         elif flag == "yyyy":
#             return int(dt_num[2])
#
#         return None
#
#     @staticmethod
#     def valid_date(dt):
#         month = Date.cost_dt_num(dt, "mm")
#
#         if month >= 1  and month <= 12:
#             print("Месяц валидный")
#         else:
#             print("Месяц не валидный")
#
#
# dt: Date = Date("12-04-2021")
#
# print(Date.cost_dt_num(dt, "yyyy"))
# Date.valid_date(dt)

#Задание 2
# class ZeroDivide(Exception):
#     def __init__(self, txt):
#         self.txt2 = txt
#
# try:
#     x: int = int(input("Введите числитель: "))
#     y: int = int(input("Введите знаменатель: "))
#
#     if y == 0:
#         raise ZeroDivide("Делить на ноль нельзя")
# except ZeroDivide as err:
#     print(err)
# else:
#     print(f"x / y = {x / y}")

#Задание 3
# class NotNumber(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# usr_list: list = [];
#
# while True:
#     usr_str: str = input("Введите число(stop для выхода): ")
#
#     try:
#         if not usr_str.isnumeric() and usr_str.lower() == 'stop':
#             break
#         elif not usr_str.isnumeric():
#             raise NotNumber("Введено не число")
#         else:
#             usr_list.append(int(usr_str))
#     except NotNumber as err:
#         print(err)
#
# print(f"Список пользователя: {usr_list}")

#Задание 4-5-6
# class Equipment:
#     def __init__(self, weight):
#         self.weight = weight
#
#
# class Printer(Equipment):
#     def __init__(self, weight, size_lists):
#         super().__init__(weight)
#         self.size_lists = size_lists
#
#
# class Scanner(Equipment):
#     def __init__(self, weight, color):
#         super().__init__(weight)
#         self.color = color
#
#
# class Xerox(Equipment):
#     def __init__(self, weight, button):
#         super().__init__(weight)
#         self.button = button
#
#
# class Store:
#     def __init__(self, storages):
#         self.storages = storages
#
#     def __init__(self):
#         self.storages = {"printer": 0, "scanner": 0, "xerox": 0}
#
#     def append_equipment(self, equipment):
#         if type(equipment) == Printer:
#             self.storages["printer"] = self.storages["printer"] + 1
#         elif type(equipment) == Scanner:
#             self.storages["scanner"] = self.storages["scanner"] + 1
#         elif type(equipment) == Xerox:
#             self.storages["xerox"] = self.storages["xerox"] + 1
#
#
# s: Store = Store()
#
# s.append_equipment(Printer(29, 10))
# s.append_equipment(Printer(30, 12))
# s.append_equipment(Printer(31, 13))
# s.append_equipment(Scanner(32, "white"))
# s.append_equipment(Scanner(33, "black"))
# s.append_equipment(Xerox(34, 2))
#
# print(s.storages)

#Задание 7
# class ComplexNum:
#     def __init__(self, a: int, b: int):
#         self.a = a
#         self.b = b
#
#     def __add__(self, other):
#         return ComplexNum(self.a + other.a, self.b + other.b)
#
#     def __mul__(self, other):
#         return ComplexNum((self.a * other.a - self.b * other.b), (self.a * other.b - other.a * self.b))
#
#     def __str__(self):
#         return f"{self.a} + {self.b}i"
#
# c1: ComplexNum = ComplexNum(1, 2)
# c2: ComplexNum = ComplexNum(2, 3)
#
# print(c1 + c2)
# print(c1 * c2)