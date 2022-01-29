#Задание 1
from sys import argv

script_name, work_hours, rate, prem = argv

print(f"Заработная плата сотрудника: {int(work_hours) * float(rate) + float(prem)}")

#Задание 2
base_list: list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def generator(lst: list):
    for i in range(1, len(lst) - 1):
        if lst[i - 1] < lst[i]:
            yield lst[i]

new_list: list = list(generator(base_list))

print(new_list)

#Задание 3
lst = list([el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0])
print(lst)

#Задание 4
base_lst: list = list([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])
new_lst: list = list([el for el in base_lst if base_lst.count(el) == 1])
print(new_lst)

#Задание 5
from functools import reduce

def mult_lst(arg_1: int, arg_2: int):
    """
    Фнукция умножения двух целочисленных аргументов
    :param arg_1: целое число
    :param arg_2: цело число
    :return: произведение чисел
    """
    return arg_1 * arg_2

lst: list = list([el for el in range(100, 1001) if el % 2 == 0])
print(f"Произведение всех чисел: {reduce(mult_lst, lst)}")

#Задание 6
from gen_num import generator_num
from gen_cycle import generator_cycle

base_list: list = list([1, 2, 3])

lst1: list = list(generator_num(10, 20))
lst2: list = list(generator_cycle(base_list, 20))

print(f"lst1: {lst1}")
print(f"lst2: {lst2}")

#Задание 7
from functools import reduce
from util import multiplication
from util import add

def fact(n: int):
    for i in range(1, n):
        t_lst = list([el for el in range(1, i + 1)])
        yield reduce(multiplication, t_lst)

cnt: list = list([0])
for el in fact(10):
    print(f"{(add(cnt)[0])}! {' * '.join([str(el) for el in range(1, cnt[0] + 1)])} = {el}")