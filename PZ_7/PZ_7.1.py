# дан символ С. вывести два символа,
# первый из которых предшествует символу С
# в кодовой таблице, а второй следует за символом С.

import random

# функция возвращает предыдущий и следующий символ
def get_neighbor_chars(C):
    try:
        # Проверяю входных данных
        if not isinstance(C, str) or len(C) != 1:
            return None, None, "Ошибка: на вход должен подаваться один символ"

        # Получает коды символов
        code = ord(C)  # Код текущего символа
        prev_code = code - 1  # Код предыдущего символа
        next_code = code + 1  # Код следующего символа

        # Конвертируем коды обратно в символы
        prev_char = chr(prev_code)
        next_char = chr(next_code)

        return prev_char, next_char
    except Exception as e:
        return None, None, f"Ошибка: {e}"
# функция генерирует случайный символ
def generate_random_char():
    # Случайно выбираем категорию символа
    category = random.randint(1, 4)

    if category == 1:
        # Случайная буква верхнего регистра (A-Z)
        return chr(random.randint(65, 90))
    elif category == 2:
        # Случайная буква нижнего регистра (a-z)
        return chr(random.randint(97, 122))
    elif category == 3:
        # Случайная цифра (0-9)
        return chr(random.randint(48, 57))
    else:  # category == 4
        # Случайный специальный символ
        special_ranges = [
            (33, 47),  # !"#$%&'()*+,-./
            (58, 64),  # :;<=>?@
            (91, 96),  # [\]^_`
            (123, 126)  # {|}~
        ]
        range_choice = random.choice(special_ranges)
        return chr(random.randint(range_choice[0], range_choice[1]))

# расчет ответов и их вывод
for i in range(5):
    # Генерация случайного символа
    random_char = generate_random_char()
    # Получение соседних символов
    prev, next_ = get_neighbor_chars(random_char)

    if prev is not None and next_ is not None:
        # Форматируем вывод для непечатных символов
        prev_display = repr(prev) if ord(prev) < 32 or ord(prev) > 126 else f"'{prev}'"
        next_display = repr(next_) if ord(next_) < 32 or ord(next_) > 126 else f"'{next_}'"
        char_display = repr(random_char) if ord(random_char) < 32 or ord(random_char) > 126 else f"'{random_char}'"
        # вывод результата
        print(f" Символ: {char_display:10} (код: {ord(random_char):3d})")
        print(f" Предыдущий: {prev_display:10} (код: {ord(prev):3d})")
        print(f" Следующий: {next_display:10} (код: {ord(next_):3d})")
    else:
        print()
