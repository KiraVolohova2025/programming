#Из исходного текстового файла (hotline.txt) перенести в первый файл строки с
#корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например,
#86532547891), а во второй с некорректными номерами телефонов. Посчитать
#полученные строки в каждом файле.
import re

# Компилирую шаблон
p = re.compile(r'\b\d{11}\b')
# Чтение строк
with open('hotline.txt', encoding='utf-8') as f:
    lines = f.readlines()
#Разделяю на корректные и некорректные
valid = list(filter(lambda x: p.search(x), lines))
invalid = list(filter(lambda x: not p.search(x), lines))
#запись в файлы
with open('valid_phones.txt', 'w', encoding='utf-8') as f:
    f.writelines(valid)
with open('invalid_phones.txt', 'w', encoding='utf-8') as f:
    f.writelines(invalid)

#Вывод результата
print(f'Корректных строк: {len(valid)}\nНекорректных строк: {len(invalid)}')