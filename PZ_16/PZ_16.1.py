"""
Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
инкремента и декремента значения.

"""

class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def increment(self):
        """Увеличивает значение счетчика на 1"""
        self.value += 1
        return self.value

    def decrement(self):
        """Уменьшает значение счетчика на 1"""
        self.value -= 1
        return self.value

    def get_value(self):
        """Возвращает текущее значение счетчика"""
        return self.value

    def reset(self):
        """Сбрасывает значение счетчика на 0"""
        self.value = 0
        return self.value

    def show_info(self):
        return f"Текущее значение счетчика: {self.value}"


# Пример использования
print("СЧЕТЧИК")
counter = Counter(5)
print(f"Начальное значение: {counter.get_value()}")
print(f"Инкремент: {counter.increment()}")
print(f"Инкремент: {counter.increment()}")
print(f"Декремент: {counter.decrement()}")
print(counter.show_info())
print(f"Сброс: {counter.reset()}")