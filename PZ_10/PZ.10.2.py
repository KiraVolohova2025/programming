# Из предложенного текстового файла вывести 
#на экран его содержимое, количество знаков 
#пунктуации в первых четырех строках. 
#Сформировать новый файл, в который поместить 
#текст в стихотворной форме предварительно 
#заменив символы третей строки их числовыми кодами.

# Чтение файла
file = open('text18-3.txt', 'r', encoding='UTF-16 LE')
lines = file.readlines()

# Вывожу содержимого файла
print("Содержимое файла:")
print("".join(lines))
print()

# Знаки возможной пунктуации для проверки
punct = """.,!?;:-'"()[]{}<>—…«»"""

# подсчет знаков пунктуации в первых четырех строках
punct_c = 0
for i in range(min(4, len(lines))):
    for char in lines[i]:
        if char in punct:
            punct_c += 1

print(f"количество знаков пунктуации в первых четырех строках: {punct_c}")

# Заменяю символы третьей строки их числовыми кодами
if len(lines) >= 3:
    t_line = lines[2]  # Индекс 2 это третья строка (счет с 0)
    cod_line = ""
    for char in t_line:
        if char != '\n':  # Не заменяю символ переноса строки
            cod_line += str(ord(char)) + " "
        else:
            cod_line += char
    
    # Создаю новый файл
file10_2 = open('text18-3_coded.txt', 'w', encoding='UTF-8')
for i, line in enumerate(lines):
    if i == 2:  # Третья строка
        file10_2.write(cod_line)
    else:
        file10_2.write(line)
    
    print("\nСоздан файл 'text18-3_coded.txt' с заменой символов третьей строки на числовые коды")

# Проверяю содержимого нового файла
print("\nСодержимое нового файла:")
file10_2 = open('text18-3_coded.txt', 'r', encoding='UTF-8')
print(file10_2.read())