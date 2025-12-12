# Дана строка, содержащая латинские буквы.
# если буквы в строке упорядочены по алфавиту,
# то вывести 0. в противном случае вывести номер
# первого символа строки, нарушающего алфавитный порядок.

import random

# функция проверяет упорядоченность букв в строке.
def check_alphabetical_order(text):
    # собирает позиции строчных букв
    l = [(i, c) for i, c in enumerate(text) if 'a' <= c <= 'z']

    # проверяю порядок
    for j in range(len(l) - 1):
        if l[j][1] > l[j + 1][1]:
            return l[j + 1][0] + 1  # +1 для индексации
    return 0


# Генерирую случайную строку
length = random.randint(8, 15)  # Случайная длина от 8 до 15 символов
random_string = ""

for _ in range(length):
    if random.random() < 0.4:  # 40% вероятность цифры
        random_string += str(random.randint(0, 9))
    else:  # 60% вероятность строчной буквы
        random_string += chr(random.randint(97, 122))

# вывод результата
print("\n Случайно сгенерированная строка:")
print(f"'{random_string}'")
print(f"Длина: {len(random_string)} символов")

# Проверяею упорядоченность букв
result = check_alphabetical_order(random_string)

print("\nРезультат проверки:")
if result == 0:
    print("Буквы в строке упорядочены по алфавиту")
else:
    print(f"Нарушение алфавитного порядка на позиции {result}")
    print(f"Символ на позиции {result}: '{random_string[result - 1]}'")
