#Даны два целых числа A и B (A < B).
#Найти сумму всех целых чисел от A до B включительно(исп. оператор цикла)

A, B = input('Введите первое число: '), input('Введите второе число: ')

while type(A) != int:
    try:
        A = int(A)
        break
    except ValueError:
        print("Неправильно ввели!")
        A = input("Введите первое число: ")

while type(B) != int:
    try:
        B = int(B)
        break
    except ValueError:
        print("Неправильно ввели!")
        B = input("Введите второе число: ")

if A >= B:
    print('Ошибка: A должно быть меньше B.')
else:
    current = B
    S = 0

    while current >= A:
        S += current
        current -= 1

print(f'Сумма всех чисел от A до B: {S}')