#Вывести первые N (N>=3) чисел Фибоначчи и посчитать количество четных чисел

N = input('Введите число N: ')

while type(N) != int or N < 3:
    try:
        N = int(N)
        if N < 3:
            print("Число меньше 3...")
            N = input('Введите число N: ')
        else:
            break
    except ValueError:
        print("Неправильный ввод!")
        N = input('Введите начальное значение: ')

a = 0
b = 1
i = 1
wanted = 0

while i <= N:
    print(a)
    if a % 2 == 0:
        wanted += 1

    c = a + b
    a = b
    b = c
    i += 1

print(f'Количество чётных чисел: {wanted}')