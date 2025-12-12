# дан список размера N. НАйти номер его первого локального минимума
# (локальный минимум - элемент, который меньше любого из своих соседей).

import random

def find_first_local_minimum(numbers):
    try:
        # Проверяю на корректность входных данных
        if not isinstance(numbers, list):
            raise TypeError("Входные данные должны быть списком")
        if len(numbers) == 0:
            raise ValueError("Список не может быть пустым")

        # Проверка, что все элементы списка - числа
        for num in numbers:
            if not isinstance(num, (int, float)):
                raise TypeError("Все элементы списка должны быть числами")
        # Обработка крайних случаев
        if len(numbers) == 1:
            # Для одного элемента нельзя определить локальный минимум
            return -1
        # проверка первого элемента (у него только правый сосед)
        if len(numbers) >= 1 and numbers[0] < numbers[1]:
            return 0
        # Проверяю элементов с 1 до n-2
        for i in range(1, len(numbers) - 1):
            if numbers[i] < numbers[i - 1] and numbers[i] < numbers[i + 1]:
                return i
        # Проверка последнего элемента (у него только левый сосед)
        if len(numbers) >= 2 and numbers[-1] < numbers[-2]:
            return len(numbers) - 1
        # если локальный минимум не найден
        return -1
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
        return -1
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
        return -1

# генерирую случайного списка
random_list = [random.randint(1, 100) for _ in range(10)]
# 10 случайных чисел от 1 до 100
# поиск локального минимума
result = find_first_local_minimum(random_list)

# Вывод результатов
print(f"Случайный список: {random_list}")
print(f"Индекс первого локального минимума: {result}")
if result != -1:
    print(f"Значение локального минимума: {random_list[result]}")
else:
    print("Локальный минимум не найден")