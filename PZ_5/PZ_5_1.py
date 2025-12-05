# Составить функцию, которая выполнит
# суммирование числового ряда.

# функция суммирует все числа числовго ряда
def Summa_count(series):
    summa = 0 # переменная будет хранить сумму
    t = 0 # инициализирую счетчик
    # цикл будет прерван когда он выйдет за предел ряда
    while True:
        try:
            current_elem = series[t]
            summa += current_elem
            t += 1
        except IndexError:
            break
    return summa
# числовой ряд, который будет суммироваться
series1 = [1, 2, 3, 4, 5]
print(f"Сумма ряда {series1} равняется {Summa_count(series1)}")
