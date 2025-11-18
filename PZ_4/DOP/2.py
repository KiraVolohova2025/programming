#Ввести 4 числа. Найти и вывести на экран количество четных чисел

a, b = input('Введите первое число: '), input('Введите второе число: ')
c, d = input('Введите третье число: '), input('Введите четвёртое число: ')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Неверный ввод числа..')
        a = input('Введите первое число: ')

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Неверный ввод числа..')
        b = input('Введите второе число: ')

while type(c) != int:
    try:
        c = int(c)
    except  ValueError:
        print('Неверный ввод числа..')
        c = input('Введите третье число: ')

while type(d) != int:
    try:
        d = int(d)
    except  ValueError:
        print('Неверный ввод числа..')
        d = input('Введите четвертое число: ')

count_numbers = 0
i = 1

while i <= 4:
    if i == 1:
        number = a
    if i == 2:
        number = b
    if i == 3:
        number = c
    if i == 4:
        number = d
    if i == 5:
        break

    if number % 2 == 0:
        count_numbers += 1

    i += 1

print(f'Кол-во четных чисел: {count_numbers}')