from itertools import count

def generator_num(a: int, b: int):
    """
    Итератор, генерирующий целые числа, начиная с указанного
    :param a: первичное число
    :param b: предел последовательности
    :return: числа
    """
    for el in count(a):
        if el > b:
            break

        yield el