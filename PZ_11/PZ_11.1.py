# организовать и вывести последовательность из N 
# случайных целых чисел. из исходной последовальености 
# организовать первую послндовательность, 
# содержащую числа кратные трем. и вторую- 
# для всех остальных. найти количество 
# элементов в полученных последовальеностях.

import random

def process_num(n):
    # генерация последовательности
    numbers = list(map(lambda x: random.randint(1, 10), range(n)))
    
    # Получаю числа через фильтр
    multi = list(filter(lambda x: x % 3 == 0, numbers))
    non_multi = list(filter(lambda x: x % 3 != 0, numbers))
    
    #Вывод результатов с прямым использованием len
    print(f"Исходная последовательность ({len(numbers)} элементов):")
    print(numbers)
    print(f"\nЧисла, кратные 3 ({len(multi)} элементов):")
    print(multi if multi else "Нет чисел, кратных 3")
    print(f"\nОстальные числа ({len(non_multi)} элементов):")
    print(non_multi if non_multi else "Нет остальных чисел")

#запуск программы
N = int(input("Введите количество чисел в последовательности:"))
process_num(N)
