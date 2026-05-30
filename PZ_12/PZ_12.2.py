# Формирование массива из положительных четных элементов,
#нахождение их суммы и среднего арифметического
from functools import reduce
import random

#Генерация случайной квадратной матрицы
n = int(input("Введите размер квадратной матрицы: "))
matrix = [[random.randint(-20, 20) for _ in range(n)] for _ in range(n)]

print("\nИсходная случайная матрица:")
list(map(lambda row: print("  ".join(map(lambda x: f"{x:4}", row))), matrix))

# склеиваю все строки в один список
flat = reduce(lambda a, b: a + b, matrix, [])
#Оставляет только числа > 0 и делящиеся на 2 без остатка
pos_e = list(filter(lambda x: x > 0 and x % 2 == 0, flat))
#складываю все отобранные числа
summa = reduce(lambda a, b: a + b, pos_e, 0) if pos_e else 0
#Среднее арифметическое
average = summa / len(pos_e) if pos_e else 0
#вывод результата
print(f"Положительные чётные элементы: {pos_e}")
print(f"Сумма: {summa}")
print(f"Среднее арифметическое: {average:.2f}" if average else "Среднее арифметическое: 0")