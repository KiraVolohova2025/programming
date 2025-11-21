#Ввести N чисел. Посчитать и вывести количество чисел, равных нулю.

n = input('Введите число: ')

while type(n) != int:
    try:
        n = int(n)
        if n <= 0:
            print("Число должно быть > 0!")
            n = input("Введите число: ")
        else:
            break
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите число: ")

i = 1
S = 0

while i <= n:

    num = input(f'Введите число {i}: ')

    while type(num) != int:
        try:
            num = int(num)
            break
        except ValueError:
            print("Неправильно ввели!")
            num = input(f'Введите число {i}: ')

    if num == 0:
        S += 1

    i += 1

print(f'Кол-во чисел, равных нулю: {S}')