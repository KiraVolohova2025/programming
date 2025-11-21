#Найти и вывести на экран S=1!+2!+...+n! (n>1).

number = input('Введите число: ')

while type(number) != int:
    try:
        number = int(number)
        if number <= 0:
            print("Число должно быть > 0!")
            number = input("Введите число: ")
        else:
            break
    except ValueError:
        print("Неправильно ввели!")
        number = input("Введите число: ")

i = 1
factorial = 1
S = 0

while i <= number:
    factorial *= i
    S += factorial
    i += 1

print(f"S = {S}")