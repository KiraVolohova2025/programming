# Дан список N (четное число).
# Поменять его первый элемент со вторым,
# третьим, четвертым и тд

import random

# Функция меняет местами элементы парами
def swap(numbers):
    try:
       # Проверка четности длины списка
        if len(numbers) % 2 != 0:
            print(f"Ошибка: список должен иметь четную длину. Длина: {len(numbers)}")
            return None
        # Создаем копию списка, чтобы не изменять оригинал
        result = numbers.copy()
        # Меняем элементы парами
        for i in range(0, len(result), 2):  # Шаг = 2
            result[i], result[i + 1] = result[i + 1], result[i]
        return result

    except IndexError:
        print("Ошибка: выход за границы списка")
        return None
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return None

# функция генерирует случайный список четной длины
def gen_random_list(min_len=2, max_len=10):
    # Генерирую случайную четную длину
    length = random.randint(min_len, max_len)
    if length % 2 != 0:
        length += 1  # делаю четной

    # генерируeт случайные числа
    return [random.randint(1, 10) for _ in range(length)]

random_list = gen_random_list(1,10)
# вывод результата
print(f"Исходный список: {random_list}")
Result = swap(random_list)
if Result:
    print(f"Результат:       {Result}")
