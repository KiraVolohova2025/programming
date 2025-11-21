#Ввести N чисел. Найти и вывести их среднее арифметическое

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
            if num <= 0:
                print("Число должно быть > 0!")
                num = input(f'Введите число {i}: ')
            else:
                break
        except ValueError:
            print("Неправильно ввели!")
            num = input(f'Введите число {i}: ')

    S += num
    i += 1

average = S / n

print(f'Среднее арифметическое: {average}')