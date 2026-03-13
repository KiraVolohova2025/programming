# составить генератор (yield) 
# который выводит из строки только цифры.

#генератор использует filter с функцией str.isdigit
#для отбора цифр
def digit_gen(t):
    yield from filter(str.isdigit, t)

user_str = input("Введите строку: ")
digits = ''.join(digit_gen(user_str))#объединяет цифры в строку

#вывод результата
print("Цифры в строке:" if digits else "В строке нет цифр.")
print(digits) if digits else None