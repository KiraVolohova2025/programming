#Посчитать и вывести количество элементов арифметической
#прогрессии, удовлетворяющих условию 10<a(i)<30.

start_number = input('Введите начальное значение: ')
step = input('Введите шаг арифметической прогрессии: ')

while type(start_number) != int:
    try:
        start_number = int(start_number)
        if start_number < 0 and start_number < 30:
            print("Число меньше 0 или меньше 30...")
            start_number = input('Введите начальное значение: ')
        else:
            break
    except ValueError:
        print("Неправильный ввод!")
        start_number = input('Введите начальное значение: ')

while type(step) != int:
    try:
        step = int(step)
        if step <= 0:
            print('Шаг меньше 0..')
            step = input('Введите шаг арифметической прогрессии: ')
    except ValueError:
        print('Неправильный ввод!')
        step = input('Введите шаг арифметической прогрессии: ')

count = 0
number = start_number - step

while number < 30:
    number += step
    if number > 10:
        count += 1

count -= 1
print(f'Количество элементов арифметической прогрессии - {count}')