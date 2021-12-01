import time

#1
class TrafficLight:
    __color = None


    def running(self):
        time_1 = time.time()
        while True:
            time_now = time.time() - time_1
            if time_now <= 7:
                print("Красный")
                time.sleep(7)
            time_now = time.time() - time_1
            if time_now > 7 and time_now <= 9:
                print("Желтый")
                time.sleep(2)
            time_now = time.time() - time_1
            if time_now > 9 and time_now < 15:
                print("Зеленый")
                time.sleep(6)
            time_now = time.time() - time_1
            if time_now > 15:
                break

# trafficLight = TrafficLight()
# trafficLight.running()

#2
class Road:
    _length = None
    _width = None

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def asphalt_mass_calc(self, weight: int, asphalt_thickness: int):
        result = (self._width * self._length * weight * asphalt_thickness) / 1000
        print(f"Масса асфальта, необходимого для покрытия всего дорожного полотна {int(result)} т.")


road = Road(20, 5000)
road.asphalt_mass_calc(25, 5)


#3

class Worker:
    name = None
    surname = None
    position = None
    _income = {"wage": 80000, "bonus": 50000}
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus
        print(f"Работник {name} {surname} добавлен в базу.")


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        name = self.name
        print(name)
    def get_total_income(self):
        profit = super()._income["wage"] + super()._income["bonus"]
        print(f"Доход сотрудника {profit}")

position = Position("Гарегин", "Папян", "Директор", 100000, 50000)


position.get_full_name()
position.get_total_income()

#4

class Car:
    speed = None
    color = None
    name = None
    is_police = False
    def __init__(self, speed: int, color: str, name: str, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        print(f"Автомобиль {name} создан")

    def go(self):
        print("Машина поехала")
    def stop(self):
        print("Машина остановилась")
    def turn(self, direction: str):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорось автомобиля {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости осторожно")
            print(f"Текущая скорось автомобиля {self.speed} км/ч")

class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости осторожно")
            print(f"Текущая скорось автомобиля {self.speed} км/ч")

class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str, isPolice: bool):
        super().__init__(speed, color, name,  isPolice)


car1 = PoliceCar(80, "черный", "мустанг", True)
car1.show_speed()
car1.go()
car1.stop()
car1.turn("направо")

car2 = SportCar(120, "черный", "феррари")
car2.show_speed()


car3 = TownCar(100, "черный", "форд")
car3.show_speed()

car4 = TownCar(100, "черный", "кадилак")
car4.show_speed()

#5

class Stationery:
    def __init__(self, title):
        self.title = title
        print(f"{title} создан")

    def draw(self):
        print(f"Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Ручка пишет")
class Pencil(Stationery):
    def draw(self):
        print("Карандаш рисует")
class Handle(Stationery):
    def draw(self):
        print("Маркер рисует")

pen = Pen("Ручка")
pen.draw()

pencil = Pencil("Карандаш")
pencil.draw()

handle = Handle("Маркер")
handle.draw()
