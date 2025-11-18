# Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа,
# расположенные между A и B (вкл. сами числа A и B), а также количество этих
# чисел (исп. оператор цикла)

a = input("Введите первое целое число:")
b = input("Введите второе целое число:")

while type(a) != int:
    try:
        a = int(a)
        break
    except ValueError:
        print("Неправильно ввели. Число должно быть целым.")
        a = input("Введите первое целое число:")

while type(b) != int:
    try:
        b = int(b)
        break
    except ValueError:
        print("Неправильно ввели. Число должно быть целым.")
        b = input("Введите второе целое число:")

if a >= b:
    print('Ошибка: первое число должно быть меньше второго.')
else:
    count = 0
    current = b

    print('Числа в порядке убывания:', end=' ')

    while current >= a:
        print(current, end=' ')
        count += 1
        current -= 1

    print()
    print('Количество чисел:', count)