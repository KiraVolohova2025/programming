# организовать и вывести последовательность из N 
# случайных целых чисел. из исходной последовальености 
# организовать первую послндовательность, 
# содержащую числа кратные трем. и вторую- 
# для всех остальных. найти количество 
# элементов в полученных последовальеностях.

import random
from functools import reduce

def process_num(n):
    # генерация последовательности
    numbers = list(map(lambda x: random.randint(1, 10), range(n)))
    
    #использую редьюс для подсчета кратных чисел
    count_multi = reduce(lambda acc, x: acc + 1 if x % 3 == 0 else acc, numbers, 0)
    
    # Получаю сами числа через фильтер
    multi = list(filter(lambda x: x % 3 == 0, numbers))
    non_multi = list(filter(lambda x: x % 3 != 0, numbers))
    
    #Вывод результатов
    print(f"Исходная последовательность ({len(numbers)} элементов):")
    print(numbers)
    print(f"\nЧисла, кратные 3 ({count_multi} элементов):")
    print(multi if multi else "Нет чисел, кратных 3")
    print(f"\nОстальные числа ({len(numbers) - count_multi} элементов):")
    print(non_multi if non_multi else "Нет остальных чисел")

# Запуск
N = int(input("Введите количество чисел в последовательности:"))
process_num(N)