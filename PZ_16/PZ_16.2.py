"""
Создайте класс "Автомобиль", который содержит информацию о марке, модели и
годе выпуска. Создайте класс "Грузовик", который наследуется от класса
"Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
"Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
информацию о количестве пассажиров.

"""

class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.brand} {self.model} заводит двигатель.")

    def stop_engine(self):
        print(f"{self.brand} {self.model} глушит двигатель.")

    def get_info(self):
        return f"{self.brand} {self.model}, {self.year} год"


class Truck(Car):
    def __init__(self, brand: str, model: str, year: int, load_capacity: float):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def load_cargo(self):
        print(f"Грузовик {self.brand} {self.model} загружает груз до {self.load_capacity} тонн.")

    def unload_cargo(self):
        print(f"Грузовик {self.brand} {self.model} выгружает груз.")

    def get_info(self):
        return f"{self.brand} {self.model}, {self.year} год, грузоподъемность: {self.load_capacity} т"


class PassengerCar(Car):
    def __init__(self, brand: str, model: str, year: int, passengers: int):
        super().__init__(brand, model, year)
        self.passengers = passengers

    def board_passengers(self):
        print(f"Легковой автомобиль {self.brand} {self.model} принимает {self.passengers} пассажиров.")

    def alight_passengers(self):
        print(f"Пассажиры выходят из {self.brand} {self.model}.")

    def get_info(self):
        return f"{self.brand} {self.model}, {self.year} год, количество пассажиров: {self.passengers}"


# Пример использования
print("ГРУЗОВИК")
truck1 = Truck(brand="Volvo", model="FH16", year=2021, load_capacity=20.5)
print(truck1.get_info())
truck1.start_engine()
truck1.load_cargo()
truck1.stop_engine()

print("\nЛЕГКОВОЙ АВТОМОБИЛЬ")
car1 = PassengerCar(brand="Toyota", model="Camry", year=2023, passengers=5)
print(car1.get_info())
car1.start_engine()
car1.board_passengers()
car1.stop_engine()