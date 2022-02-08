#Задание 1
name_file: str = input("Введите наименование файла: ")

with open(name_file, "w+") as file:
    while True:
        usr_str: str = input("Введите строку: ")

        if len(usr_str) == 0:
            break;

        file.write(usr_str + "\n")

#Задание 2
cnt_row: int = 0 #Кол-во строк
cnt_words: int = 0 #Кол-во слов

word_in_row: dict = dict()

with open("file_task_2.txt", "r") as file:
    for txt in file.readlines():
        cnt_row += 1
        word_in_row[cnt_row] = len(list(txt.split(" ")))

print(f"Кол-во строк: {cnt_row}")
for i in range(1, cnt_row + 1):
    print(f"Кол-во слов {word_in_row[i]} в строке {i}")

#Задание 3
sum: float = 0 #Полня сумма зарплаты
cnt: int = 0 #Кол-во сотрудников в файле
agr_sum: float = 0 #Средняя зарплата сотрдуников

with open("file_task_3.txt",  mode="r", encoding="utf-8") as file:
    for txt in file:
        cnt += 1

        flist: list = txt.split(" ")
        if float(flist[1]) < 20000:
            print(f"Сотрудник: {flist[0]}, Зарплата: {flist[1]}")

        sum += float(flist[1])

agr_sum = round(sum / cnt, 2)
print(f"Средняя зарплата сотрудников: {agr_sum}")

#Задание 4
def trans_line(line: str):
    return {
        line.upper().find("ONE") != -1: line.upper().replace("ONE", "Один").title(),
        line.upper().find("TWO") != -1: line.upper().replace("TWO", "Два").title(),
        line.upper().find("THREE") != -1: line.upper().replace("THREE", "Три").title(),
        line.upper().find("FOUR") != -1: line.upper().replace("FOUR", "Четыре").title()
    }[True]

with open("file_task_4.txt", "r") as rfile:
    for txt in rfile:
        with open("file_task_4_1.txt", "a") as wfile:
            wfile.write(trans_line(txt))

#Задание 5
from random import randint

def create_file():
    with open("file_task_5.txt", "w") as rfile:
        for i in range(1, 10):
            if i != 9:
                rfile.write(f"{randint(1, 10)} ")
            else:
                rfile.write(f"{randint(1, 10)}")

asum: int = 0

create_file()

with open("file_task_5.txt", "r") as rfile:
    asum = sum(list(map(int, rfile.readline().split(" "))))

print(f"Total sum: {asum}")

#Задание 6
def get_num_list(val: str):
    if val == "-" or len(val) == 0:
        return 0
    else:
        return int(val[0:val.find("(")])

items: dict = dict()

with open("file_task_6.txt", "r", encoding="utf-8") as rfile:
     for s in rfile:
         key = s.split(":")[0]
         lsum = sum(list(map(get_num_list, s.split(":")[1].split(" "))))
         items[key] = lsum

print(items)

#Задание 7
import json

d_prof: dict = dict()
cnt: int = 0

def minus_zero(val: float):
    global cnt

    if val < 0:
        return 0

    cnt += 1
    return val

with open("file_task_7.txt", "r") as rfile:
    for s in rfile:
        inf: list = list(s.split(" "))
        d_prof[inf[0]] = float(inf[2]) - float(inf[3])

average_profit: float = round(sum(list(map(minus_zero, d_prof.values()))) / cnt, 2)

d_average_profit: dict = {"average_profit": average_profit}

data: list = [d_prof, d_average_profit]

with open("file_task_7.json", "w") as wfile:
    json.dump(data, wfile)

