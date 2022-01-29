def cont_prc():
    str = input("Продолжить (Y/N): ")
    if str != 'Y':
        return True
    else:
        return False


#Задание 1
# def division(arg_1: float, arg_2: float):
#     """
#     Возвращает результат деления arg_1 на arg_2
#     Пердусомтрено деление на 0
#
#     :param arg_1: аргумент 1
#     :param arg_2: аргумент 2
#     :return:  результат деления
#     """
#     try:
#         return arg_1 / arg_2
#     except ZeroDivisionError:
#         return None
#
# while True:
#     arg_1 = float(input("Введите первое число: "))
#     arg_2 = float(input("Введите второе число: "))
#     print(f"Результат деления чисел: {division(arg_1 = arg_1, arg_2 = arg_2)}")
#     if cont_prc():
#         break;
#
#Задание 2
# def print_inf_user(name: str, lastname: str, birthdate: str, city: str, email: str, phone: str):
#     """
#     Вывод информации о пользователе
#
#     :param name: Имя
#     :param lastname: Фамилия
#     :param birthdate: Дата рождения
#     :param city: Город
#     :param email: Email
#     :param phone: Телефон
#     :return:
#     """
#     print("Данные пользователя:")
#     print(f"  Имя: {name}, Фамилия: {lastname}, Год рождения: {birthdate}, Город: {city}, Email: {email}, Телефон: {phone}")
#     pass
#
# while True:
#     print("Введите данные пользователя")
#
#     print_inf_user(name = input("Имя: "), lastname = input("Фамилия: "), birthdate = input("Дата рождения: "), city = input("Город: "), email = input("Email: "), phone = input("Телефон: "))
#     if cont_prc():
#         break;
#
#Задание 3
# def my_func(arg_1: int, arg_2: int, arg_3: int):
#     """
#     Возвращает сумму двух наибольших аргументов
#
#     :param arg_1: аргумент 1
#     :param arg_2: аргумент 2
#     :param arg_3: аргумент 3
#     :return: сумма больших двух аргументов
#     """
#     return sum((arg_1, arg_2, arg_3)) - min((arg_1, arg_2, arg_3))
#
# while True:
#     print(f"Сумма двух наибольших чисeл: {my_func(arg_1 = int(input('Введите 1-ое число: ')), arg_2 = int(input('Введите 2-ое число: ')), arg_3 = int(input('Введите 3-е число: ')))}");
#     if cont_prc():
#         break;
#
#Задание 4
# def my_func(x: int, y: int):
#     """
#     Возведение числа в отрицательную степень
#     :param x: число, которое возводиться в степень
#     :param y: степень числа
#     :return: результат возведения в степень
#     """
#     res: int = 1
#     for el in range(y, 0):
#         res = res * (1 / x)
#
#     return res
#
# while True:
#     x: int = int(input("Введите целое число: "))
#     y: int = int(input("Введите отрицательное число: "))
#     print(f"Результат возведения в отрицательную степень: {round(my_func(x = x, y = y), 3)}")
#     if cont_prc():
#         break;
#
#Задание 5
# global_res: int = 0
# mark: str = '--'
#
# def cost_int(arg_1: str):
#     """
#     Преобразование символа в тип int
#     Если произошла ошибка преобразования, возвращается 0
#     :param arg_1: строка
#     :return: преобразованная строка в число
#     """
#     try:
#         return int(arg_1)
#     except ValueError:
#         return 0
#
# def sum_num_usr(args: list):
#     """
#     Возвращает сумму чисел в кортеже.
#     Преобразует каждный элемент кортежа в число.
#     :param args: Кортеж
#     :return: Сумма чисел внутри кортежа
#     """
#     global global_res #Ильяс, подскажите поалуйста, почему приходится исопльзовать конструкцию global, чтобы не возникала ошибка: local variable 'global_res' referenced before assignment
#                       #Данная переменная объявлена в глобальной области видимости
#     for el in args:
#         global_res += cost_int(el.strip())
#
#     return global_res
#
# while True:
#     str = input("Введите ряд целых чисел разделенных пробелам: ")
#     if str.find(mark) != -1:
#         str = str[0 : str.find(mark)]
#         print(f"Результат работы: {sum_num_usr(str.split(' '))}")
#         break
#
#     print(f"Сумма чисел на данный момент: {sum_num_usr(str.split(' '))}")
#
#Задание 6-7
# def int_func(usr_str: str):
#     return usr_str.title()
#
# while True:
#     usr_str = input("Введите строку: ")
#     print(int_func(usr_str = usr_str))
#     if cont_prc():
#         break;

