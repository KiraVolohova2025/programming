import tkinter as tk
from tkinter import ttk, messagebox
#Анкета Web-разработчика 
root = tk.Tk()
root.title("Анкета Web-разработчика")
root.geometry("600" + "x" + "550")
root.configure(bg="#D5D5D5")  # Основной фон кнопок и форм
# Основная рамка
main_frame = tk.Frame(root, bg="#D5D5D5", padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)
# Заголовок без фона
title = tk.Label(main_frame, text="Анкета Web-разработчика", font=("Arial", 14, "bold"), 
                 bg="#D5D5D5", fg="#000000")
title.pack(pady=(0, 20))
# Цвет для полей ввода
entry_bg = "#e2debc"
# егистрационное имя 
name_frame = tk.Frame(main_frame, bg="#e2debc", padx=10, pady=5)
name_frame.pack(fill=tk.X, pady=5)
tk.Label(name_frame, text="Регистрационное имя", font=("Arial", 10), 
         bg="#e2debc", width=20, anchor="w").pack(side=tk.LEFT)
name_entry = tk.Entry(name_frame, font=("Arial", 10), width=30, bg="#D5D5D5", relief="sunken", bd=1)
name_entry.pack(side=tk.LEFT, padx=10)
# Пароль 
pass_frame = tk.Frame(main_frame, bg="#e2debc", padx=10, pady=5)
pass_frame.pack(fill=tk.X, pady=5)
tk.Label(pass_frame, text="Пароль", font=("Arial", 10), 
         bg="#e2debc", width=20, anchor="w").pack(side=tk.LEFT)
pass_entry = tk.Entry(pass_frame, font=("Arial", 10), width=30, bg="#D5D5D5", relief="sunken", bd=1, show="*")
pass_entry.pack(side=tk.LEFT, padx=10)
# Ваша специализация 
spec_frame = tk.Frame(main_frame, bg="#e2debc", padx=10, pady=5)
spec_frame.pack(fill=tk.X, pady=5)
tk.Label(spec_frame, text="Ваша специализация", font=("Arial", 10), 
         bg="#e2debc", width=20, anchor="w").pack(side=tk.LEFT)
spec_combo = ttk.Combobox(spec_frame, values=["Web-мастер", "Frontend-разработчик", "Backend-разработчик", 
                                               "Fullstack-разработчик", "UI/UX-дизайнер"], 
                          width=28, state="readonly")
spec_combo.set("Web-мастер")
spec_combo.pack(side=tk.LEFT, padx=10)
# Пол 
gender_frame = tk.Frame(main_frame, bg="#D5D5D5")
gender_frame.pack(fill=tk.X, pady=5)
tk.Label(gender_frame, text="Пол", font=("Arial", 10), 
         bg="#D5D5D5", width=20, anchor="w").pack(side=tk.LEFT)
gender_var = tk.StringVar(value="М")
male_rb = tk.Radiobutton(gender_frame, text="М", variable=gender_var, value="М", 
                         bg="#D5D5D5", font=("Arial", 10))
female_rb = tk.Radiobutton(gender_frame, text="Ж", variable=gender_var, value="Ж", 
                           bg="#D5D5D5", font=("Arial", 10))
male_rb.pack(side=tk.LEFT, padx=(10, 15))
female_rb.pack(side=tk.LEFT)
#Ваши навыки 
skills_container = tk.Frame(main_frame, bg="#e2debc", padx=10, pady=10)
skills_container.pack(fill=tk.X, pady=10)
# Заголовок внутри контейнера
tk.Label(skills_container, text="Ваши навыки", font=("Arial", 10, "bold"), 
         bg="#e2debc").pack(anchor="w", pady=(0, 10))
# Фрейм для двух колонок
skills_frame = tk.Frame(skills_container, bg="#e2debc")
skills_frame.pack(fill=tk.X)

skills_list = [
    "знание HTML и CSS",
    "знание Perl",
    "знание ASP",
    "знание Adobe Photoshop",
    "знание JAVA",
    "знание JavaScript",
    "знание Flash"
]

# 1 колонка
left_col = tk.Frame(skills_frame, bg="#e2debc")
left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# 2 колонка (перечень навыков)
right_col = tk.Frame(skills_frame, bg="#e2debc")
right_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
skills_vars = {}
for i, skill in enumerate(skills_list):
    var = tk.BooleanVar()
    skills_vars[skill] = var
    # Первые 3 навыка в левую колонку, остальные 4 в правую
    if i < 3:
        col = left_col
    else:
        col = right_col
    cb = tk.Checkbutton(col, text=skill, variable=var, bg="#e2debc", 
                        font=("Arial", 9), anchor="w")
    cb.pack(anchor="w", pady=3)

info_container = tk.Frame(main_frame, bg="#e2debc", padx=10, pady=10)
info_container.pack(fill=tk.BOTH, expand=True, pady=10)

# Левая колонка текст
left_info = tk.Frame(info_container, bg="#e2debc", width=150)
left_info.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
left_info.pack_propagate(False)

tk.Label(left_info, text="Дополнительные сведения о себе", font=("Arial", 10), 
         bg="#e2debc", wraplength=120, justify="left").pack(anchor="w", pady=10)

#текстовое поле с прокруткой
right_info = tk.Frame(info_container, bg="#e2debc")
right_info.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Текстовое поле с прокруткой
info_text = tk.Text(right_info, height=6, width=40, font=("Arial", 10), 
                    bg="#D5D5D5", relief="sunken", bd=1, wrap=tk.WORD)
scrollbar = tk.Scrollbar(right_info, orient="vertical", command=info_text.yview)
info_text.configure(yscrollcommand=scrollbar.set)

info_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# --- Кнопки ---
buttons_frame = tk.Frame(main_frame, bg="#D5D5D5")
buttons_frame.pack(fill=tk.X, pady=20)

def register():
    """Обработчик регистрации"""
    name = name_entry.get().strip()
    password = pass_entry.get().strip()
    selected_skills = [skill for skill, var in skills_vars.items() if var.get()]
    
    if not name or not password:
        messagebox.showwarning("Ошибка", "Пожалуйста, заполните все обязательные поля!")
        return
    msg = "Регистрация успешно завершена!\n\n"
    msg += f"Регистрационное имя: {name}\n"
    msg += f"Специализация: {spec_combo.get()}\n"
    msg += f"Пол: {gender_var.get()}\n"
    msg += f"Навыки: {', '.join(selected_skills) if selected_skills else 'не указаны'}\n"
    msg += f"Доп. сведения: {info_text.get('1.0', tk.END).strip() or 'не указаны'}"
    messagebox.showinfo("Регистрация", msg)

def clear_form():
    """Очистка формы"""
    name_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)
    spec_combo.set("Web-мастер")
    gender_var.set("М")
    for var in skills_vars.values():
        var.set(False)
    info_text.delete("1.0", tk.END)
# Кнопки
register_btn = tk.Button(buttons_frame, text="зарегистрировать", command=register,
                         bg="#D5D5D5", font=("Arial", 10), padx=15, pady=5,
                         relief="raised", bd=1, cursor="hand2", fg="#000000")
clear_btn = tk.Button(buttons_frame, text="очистить форму", command=clear_form,
                      bg="#D5D5D5", font=("Arial", 10), padx=15, pady=5,
                      relief="raised", bd=1, cursor="hand2", fg="#000000")

register_btn.pack(side=tk.LEFT, padx=(0, 20))
clear_btn.pack(side=tk.LEFT)
# Разделительная линия
separator = tk.Frame(main_frame, height=2, bg="#888888")
separator.pack(fill=tk.X, pady=(10, 0))

# Запуск приложения
root.mainloop()