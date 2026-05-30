#В квадратной матрице элементы на главной диагонали увеличить в 2 раза
from functools import reduce
import random

# Генерация случайной квадратной матрицы
n = int(input("Введите размер квадратной матрицы: "))
matrix = [[random.randint(-20, 20) for _ in range(n)] for _ in range(n)]
#создаю исходную матрицу
print("\nИсходная случайная матрица:")
list(map(lambda row: print("  ".join(map(lambda x: f"{x:4}", row))), matrix))

#Внешний map перебирает строки (индекс i), 
# внутренний map перебирает столбцы (индекс j) в каждой строке. 
# условие if i == j определяет диагональный элемент. 
#list() преобразует результат в матрицу.
result = list(map(lambda i: list(map(lambda j: matrix[i][j] * 2 if i == j else matrix[i][j], range(n))), range(n)))

print("\nМатрица с увеличением главной диагонали в 2 раза:")
list(map(lambda row: print("  ".join(map(lambda x: f"{x:4}", row))), result))