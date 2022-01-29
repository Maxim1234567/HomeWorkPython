from itertools import cycle

def generator_cycle(lst: list, b: int):
    """
    Итератор, повторяющий элменты некоторого списка
    :param lst: Список со значениями
    :param b: предел последовательность
    :return: значения
    """
    cnt = 0
    for el in cycle(lst):
        if cnt > b:
            break;

        cnt += 1
        yield el