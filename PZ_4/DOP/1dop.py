# Ввести 4 числа. Найти  и вывести на экран сумму
# и количество отрицательных чисел.
a = input("Введите первое число:")
b = input("Введите второе число:")
c = input("Введите третье число:")
d = input("Введите четвертое число:")

while type(a) != int:
    try:
        a = int(a)
    except Exception as e:
        print('Неверный ввод числа..')
        a = input('Введите первое число: ')

while type(b) != int:
    try:
        b = int(b)
    except Exception as e:
        print("Неверный ввод числа..")
        b = input("Введите второе число: ")

while type(c) != int:
    try:
        c = int(c)
    except Exception as e:
        print("Неверный ввод числа..")
        three = input("Введите третье число: ")

while type(d) != int:
    try:
        d = int(d)
    except Exception as e:
        print("Неверный ввод числа..")
        d = input("Введите четвертое число: ")

sum = 0
count = 0
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

    if number < 0:
        sum += number
        count += 1

    i += 1

print(f'Сумма негативных чисел: {sum}. Кол-во негативных чисел: {count}')