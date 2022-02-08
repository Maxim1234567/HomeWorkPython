#Задание 1
import time
import sys

class TrafficLight:
    def __init__(self, color: str):
        self.__color = color

    def running(self, color: str):
        if color == "red" and self.__color == "green":
            print("Красный: 7 секунд")
            time.sleep(7)
        elif color == "yellow" and self.__color == "red":
            print("Жёлтый: 2 секунды")
            time.sleep(2)
        elif color == "green" and self.__color == "yellow":
            print("Зелёный: 10 секунд")
            time.sleep(10)
        else:
            print("Нарушен режим светофора")
            sys.exit(0)

        self.__color = color

t = TrafficLight("green")

t.running("red")
t.running("yellow")
t.running("green")

t.running("red")
t.running("yellow")
t.running("green")

t.running("red")
t.running("yellow")
t.running("red")

t.running("red")
t.running("yellow")
t.running("green")

#Задание 2
class Road:
    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    def calc_mass_asphalt(self, mass_asphalt: float, depth: float):
        return self._length * self._width * mass_asphalt * depth

r: Road = Road(5000, 20)
print(r.calc_mass_asphalt(25, 5))

#Задание 3
class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, income: dict):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self.surname + ", " + self.name

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

p: Position = Position("Ivanov", "Ivan", "Programmer", {"wage": 240000, "bonus": 20000})
print(p.get_full_name())
print(p.get_total_income())

#Задание 4
class Car:
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction: str):
        print(f"Машина {self.name} повернула: {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.name} автомобиля: {self.speed}")

class TownCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость для {self.name} превышена")
        else:
            print(f"Текущая скорость {self.name} автомобиля: {self.speed}")

class SportCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость для {self.name} превышена")
        else:
            print(f"Текущая скорость {self.name} автомобиля: {self.speed}")

class PoliceCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

town: TownCar = TownCar(45, "red", "Городская", False)
sport: SportCar = SportCar(150, "black", "Спортивная", False)
work: WorkCar = WorkCar(50, "yellow", "Рабочая", False)
police: PoliceCar = PoliceCar(100, "white", "Полицейская", True)

town.go()
town.turn("right")
town.show_speed()
town.stop()

sport.go()
sport.turn("left")
sport.show_speed()
sport.stop()

work.go()
work.turn("top")
work.show_speed()
work.stop()

police.go()
police.turn("bottom")
police.show_speed()
police.stop()

#Задание 5
class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки карандашом")

class Handle(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки маркером")

pen: Pen = Pen("Ручка")
pencil: Pencil = Pencil("Карандаш")
handle: Handle = Handle("Маркер")

pen.draw()
pencil.draw()
handle.draw()