"""
Приложение КАФЕДРА для автоматизации работы отдела кадров ВУЗа.
Таблица Преподавательский состав содержит следующие данные:
Табельный номер, Фамилия И.О., Дата рождения, Должность, Ученая степень, Нагрузка, Зарплата.
"""
import sqlite3 as sq
import os

DB = "department_v1.db"

def init_db():
    """Инициализация базы данных с тестовыми данными"""
    if os.path.exists(DB):
        os.remove(DB)
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE Teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tab_number TEXT UNIQUE NOT NULL,
            full_name TEXT NOT NULL,
            birth_date TEXT,
            position TEXT NOT NULL,
            academic_degree TEXT,
            workload INTEGER DEFAULT 0,
            salary REAL DEFAULT 0
        )""")
        
        # Тестовые данные
        data = [
            ("T001", "Иванов И.И.", "1980-05-15", "Профессор", "Доктор наук", 1.0, 150000),
            ("T002", "Петрова А.С.", "1985-08-22", "Доцент", "Кандидат наук", 1.0, 120000),
            ("T003", "Сидоров В.П.", "1990-02-10", "Старший преподаватель", None, 1.5, 90000),
            ("T004", "Кузнецова Е.Н.", "1975-11-03", "Заведующий кафедрой", "Доктор наук", 0.75, 180000),
            ("T005", "Михайлов Д.А.", "1988-07-19", "Ассистент", None, 1.0, 70000),
            ("T006", "Соколова О.В.", "1982-03-27", "Доцент", "Кандидат наук", 1.25, 110000),
            ("T007", "Волков Р.С.", "1995-09-14", "Ассистент", None, 1.0, 65000),
            ("T008", "Морозова Т.И.", "1978-12-01", "Профессор", "Доктор наук", 0.5, 140000),
        ]
        cur.executemany("""
            INSERT INTO Teachers (tab_number, full_name, birth_date, position, academic_degree, workload, salary)
            VALUES (?,?,?,?,?,?,?)
        """, data)

def show_all():
    """Показать всех преподавателей"""
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Teachers")
        rows = cur.fetchall()
        if not rows:
            print("Список преподавателей пуст.")
        else:
            print("\n" + "="*100)
            print(f"{'ID':<3} {'Таб.номер':<10} {'Фамилия И.О.':<20} {'Дата рожд.':<12} {'Должность':<22} {'Уч.степень':<15} {'Нагрузка':<9} {'Зарплата':<10}")
            print("="*100)
            for row in rows:
                print(f"{row[0]:<3} {row[1]:<10} {row[2]:<20} {row[3] or '—':<12} {row[4]:<22} {row[5] or '—':<15} {row[6]:<9} {row[7]:<10.2f}")
            print("="*100)

def search_by_name():
    """Поиск по фамилии"""
    name = input("Введите фамилию (или часть): ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Teachers WHERE full_name LIKE ?", (f"%{name}%",))
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("Преподаватели не найдены.")

def search_by_position_degree():
    """Поиск по должности и ученой степени"""
    position = input("Должность: ")
    degree = input("Ученая степень (оставьте пустым для любого): ")
    
    if degree:
        query = "SELECT * FROM Teachers WHERE position = ? AND academic_degree = ?"
        params = (position, degree)
    else:
        query = "SELECT * FROM Teachers WHERE position = ?"
        params = (position,)
    
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute(query, params)
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("Преподаватели не найдены.")

def search_by_salary_range():
    """Поиск по диапазону зарплаты"""
    try:
        min_salary = float(input("Мин. зарплата: "))
        max_salary = float(input("Макс. зарплата: "))
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Teachers WHERE salary BETWEEN ? AND ?", (min_salary, max_salary))
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("Преподаватели не найдены.")
    except ValueError:
        print("Некорректное значение зарплаты.")

def edit_position():
    """Изменить должность по табельному номеру"""
    tab_num = input("Табельный номер: ")
    new_position = input("Новая должность: ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("UPDATE Teachers SET position = ? WHERE tab_number = ?", (new_position, tab_num))
        print("Должность обновлена." if cur.rowcount else "Преподаватель не найден.")

def edit_salary():
    """Изменить зарплату по должности"""
    position = input("Должность: ")
    percent = float(input("Процент изменения (например, 10 для +10%, -5 для -5%): "))
    
    with sq.connect(DB) as con:
        cur = con.cursor()
        # Сначала покажем, кого затронет изменение
        cur.execute("SELECT full_name, position, salary FROM Teachers WHERE position = ?", (position,))
        affected = cur.fetchall()
        if not affected:
            print("Преподаватели с такой должностью не найдены.")
            return
        
        print("\nБудут изменены зарплаты:")
        for row in affected:
            print(f"  {row[0]} — {row[1]}: текущая {row[2]:.2f}")
        
        confirm = input(f"\nПрименить изменение на {percent}%? (да/нет): ")
        if confirm.lower() == 'да':
            cur.execute("""
                UPDATE Teachers 
                SET salary = salary * (1 + ?/100) 
                WHERE position = ?
            """, (percent, position))
            print(f"Обновлено записей: {cur.rowcount}")

def edit_workload():
    """Изменить нагрузку по ученой степени"""
    degree = input("Ученая степень: ")
    new_workload = float(input("Новая нагрузка (например, 1.0): "))
    
    with sq.connect(DB) as con:
        cur = con.cursor()
        if degree.lower() == "нет" or degree == "":
            cur.execute("UPDATE Teachers SET workload = ? WHERE academic_degree IS NULL", (new_workload,))
        else:
            cur.execute("UPDATE Teachers SET workload = ? WHERE academic_degree = ?", (new_workload, degree))
        print(f"Обновлено записей: {cur.rowcount}")

def delete_by_tab_number():
    """Удалить по табельному номеру"""
    tab_num = input("Табельный номер для удаления: ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM Teachers WHERE tab_number = ?", (tab_num,))
        print(f"Удалено записей: {cur.rowcount}")

def delete_by_position():
    """Удалить всех по должности"""
    position = input("Должность для удаления: ")
    confirm = input(f"Вы уверены, что хотите удалить всех {position}? (да/нет): ")
    if confirm.lower() == 'да':
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Teachers WHERE position = ?", (position,))
            print(f"Удалено записей: {cur.rowcount}")

def delete_by_workload():
    """Удалить по нагрузке (меньше указанной)"""
    try:
        min_workload = float(input("Удалить преподавателей с нагрузкой МЕНЬШЕ: "))
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Teachers WHERE workload < ?", (min_workload,))
            print(f"Удалено записей: {cur.rowcount}")
    except ValueError:
        print("Некорректное значение нагрузки.")

# Инициализация БД
init_db()

# Главное меню
while True:
    print("\n" + "="*50)
    print("        МЕНЮ КАФЕДРА")
    print("="*50)
    print("1  - Показать всех преподавателей")
    print("2  - Поиск по фамилии")
    print("3  - Поиск по должности и ученой степени")
    print("4  - Поиск по диапазону зарплаты")
    print("5  - Изменить должность по табельному номеру")
    print("6  - Изменить зарплату по должности (%)")
    print("7  - Изменить нагрузку по ученой степени")
    print("8  - Удалить по табельному номеру")
    print("9  - Удалить всех по должности")
    print("10 - Удалить по нагрузке (< значение)")
    print("0  - Выход")
    print("-"*50)

    cmd = input("Выберите действие: ")

    if cmd == '1':
        show_all()
    elif cmd == '2':
        search_by_name()
    elif cmd == '3':
        search_by_position_degree()
    elif cmd == '4':
        search_by_salary_range()
    elif cmd == '5':
        edit_position()
    elif cmd == '6':
        edit_salary()
    elif cmd == '7':
        edit_workload()
    elif cmd == '8':
        delete_by_tab_number()
    elif cmd == '9':
        delete_by_position()
    elif cmd == '10':
        delete_by_workload()
    elif cmd == '0':
        print("До свидания!")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")