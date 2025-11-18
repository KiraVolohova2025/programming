#Найти и вывести на экран квадраты и кубы чисел от 2 до 5.

i = 1

while True:
    if i == 1:
        number = 2
    if i == 2:
        number = 3
    if i == 3:
        number = 4
    if i == 4:
        number = 5
    if i == 5:
        break

    use_1 = number ** 2
    use_2 = number ** 3

    print(f'Квадрат числа {number} - {use_1}, куб числа {number} - {use_2}')

    i += 1