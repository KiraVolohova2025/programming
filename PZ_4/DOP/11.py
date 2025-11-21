#Дана арифметическая прогрессия(a1=1, a2=4, a3=7, a4=10, a5=10)
#Составить программу, которая каждый элемент прогрессии разделит на 2
#и результат округлит до ближайшего целого

start_number = 1
n = 1

while n <= 15:
    result = (start_number // 2)

    if (start_number % 2) >= 0.5:
        result += 1

    print(result)
    start_number += 3
    n += 1