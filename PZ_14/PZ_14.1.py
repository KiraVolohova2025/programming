"""
Вариант 3
Анкета Web-разработчика
"""

import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    name = entry_name.get()
    password = entry_password.get()
    password_confirm = entry_password_confirm.get()
    specialization = specialization_var.get()
    gender = gender_var.get()

    if password != password_confirm:
        messagebox.showerror("Ошибка", "Пароль и подтверждение пароля не совпадают!")
        return
    skills = []
    if var_html.get(): skills.append("знание HTML и CSS")
    if var_perl.get(): skills.append("знание Perl")
    if var_asp.get(): skills.append("знание ASP")
    if var_pshop.get(): skills.append("знание Adobe Photoshop")
    if var_java.get(): skills.append("знание JAVA")
    if var_js.get(): skills.append("знание JavaScript")
    if var_flash.get(): skills.append("знание Flash")

    additional = text_additional.get("1.0", tk.END).strip()
    msg = f"""Анкета Web-разработчика

Регистрационное имя: {name}
Пароль: {password}
Специализация: {specialization}
Пол: {gender}
Навыки: {', '.join(skills) if skills else 'не выбраны'}
Дополнительные сведения: {additional}"""
    messagebox.showinfo("Регистрация", msg)

def clear_form():
    entry_name.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_password_confirm.delete(0, tk.END)
    specialization_var.set("Web-мастер")
    gender_var.set("М")
    var_html.set(False)
    var_perl.set(False)
    var_asp.set(False)
    var_pshop.set(False)
    var_java.set(False)
    var_js.set(False)
    var_flash.set(False)
    text_additional.delete("1.0", tk.END)

root = tk.Tk()
root.title("Анкета Web-разработчика")
root.geometry("550x560")
root.configure(bg="white")

title = tk.Label(root, text="Анкета Web-разработчика",
                 font=("Arial", 16, "bold"), bg="white")
title.pack(pady=(15, 10))

main_frame = tk.Frame(root, bg="white")
main_frame.pack(padx=1, pady=1, fill="both", expand=True)
main_frame.columnconfigure(0, weight=0)
main_frame.columnconfigure(1, weight=1)
#Регистрационное имя 
lbl_name = tk.Label(main_frame, text="Регистрационное имя",
                    font=("Arial", 10), bg="#e2debc", relief="solid", bd=1)
lbl_name.grid(row=0, column=0, sticky="nsew", pady=0, padx=(0, 0))

frame_name = tk.Frame(main_frame, bg="#d3d3d3", relief="solid", bd=1)
frame_name.grid(row=0, column=1, sticky="ew", pady=0, padx=(0, 0))
entry_name = tk.Entry(frame_name, font=("Arial", 10), bg="white", relief="solid", bd=1, width=30)
entry_name.pack(side="left", padx=2, pady=2)
#Пароль 
lbl_pass = tk.Label(main_frame, text="Пароль", font=("Arial", 10),
                    bg="#e2debc", relief="solid", bd=1)
lbl_pass.grid(row=1, column=0, sticky="nsew", pady=0, padx=(0, 0))

frame_pass = tk.Frame(main_frame, bg="#d3d3d3", relief="solid", bd=1)
frame_pass.grid(row=1, column=1, sticky="ew", pady=0, padx=(0, 0))
entry_password = tk.Entry(frame_pass, show="*", font=("Arial", 10),
                          bg="white", relief="solid", bd=1, width=30)
entry_password.pack(side="left", padx=2, pady=2)
#Подтверждение пароля
lbl_confirm = tk.Label(main_frame, text="Подтверждение пароля", font=("Arial", 10),
                       bg="#e2debc", relief="solid", bd=1)
lbl_confirm.grid(row=2, column=0, sticky="nsew", pady=0, padx=(0, 0))

frame_confirm = tk.Frame(main_frame, bg="#d3d3d3", relief="solid", bd=1)
frame_confirm.grid(row=2, column=1, sticky="ew", pady=0, padx=(0, 0))
entry_password_confirm = tk.Entry(frame_confirm, show="*", font=("Arial", 10),
                                  bg="white", relief="solid", bd=1, width=30)
entry_password_confirm.pack(side="left", padx=2, pady=2)
#Специализация
lbl_spec = tk.Label(main_frame, text="Ваша специализация", font=("Arial", 10),
                    bg="#e2debc", relief="solid", bd=1)
lbl_spec.grid(row=3, column=0, sticky="nsew", pady=0, padx=(0, 0))

frame_spec = tk.Frame(main_frame, bg="#d3d3d3", relief="solid", bd=1)
frame_spec.grid(row=3, column=1, sticky="ew", pady=0, padx=(0, 0))
specialization_var = tk.StringVar(value="Web-мастер")
combo_spec = ttk.Combobox(frame_spec, textvariable=specialization_var,
                          values=["Web-мастер", "Frontend-разработчик",
                                  "Backend-разработчик", "Fullstack-разработчик"],
                          state="readonly", font=("Arial", 10), width=28)
combo_spec.pack(side="left", padx=2, pady=2)

# Пол
lbl_gender = tk.Label(main_frame, text="Пол", font=("Arial", 10),
                      bg="#e2debc", relief="solid", bd=1)
lbl_gender.grid(row=4, column=0, sticky="nsew", pady=0, padx=(0, 0))

frame_gender = tk.Frame(main_frame, bg="#d3d3d3", relief="solid", bd=1)
frame_gender.grid(row=4, column=1, sticky="ew", pady=0, padx=(0, 0))
gender_var = tk.StringVar(value="М")
rb_m = tk.Radiobutton(frame_gender, text="М", variable=gender_var, value="М",
                      bg="white", activebackground="white", relief="flat")
rb_m.pack(side="left", padx=(2, 20), pady=2)
rb_f = tk.Radiobutton(frame_gender, text="Ж", variable=gender_var, value="Ж",
                      bg="white", activebackground="white", relief="flat")
rb_f.pack(side="left", padx=(0, 2), pady=2)

#Ваши навыки 
lbl_skills = tk.Label(main_frame, text="Ваши навыки", font=("Arial", 10),
                      bg="#e2debc", relief="solid", bd=1)
lbl_skills.grid(row=5, column=0, sticky="nsew", pady=0, padx=(0, 0))

frame_skills = tk.Frame(main_frame, bg="#d3d3d3", relief="solid", bd=1)
frame_skills.grid(row=5, column=1, sticky="ew", pady=0, padx=(0, 0))

var_html = tk.BooleanVar()
var_perl = tk.BooleanVar()
var_asp = tk.BooleanVar()
var_pshop = tk.BooleanVar()
var_java = tk.BooleanVar()
var_js = tk.BooleanVar()
var_flash = tk.BooleanVar()

skills = [
    ("- знание HTML и CSS", var_html),
    ("- знание Perl", var_perl),
    ("- знание ASP", var_asp),
    ("- знание Adobe Photoshop", var_pshop),
    ("- знание JAVA", var_java),
    ("- знание JavaScript", var_js),
    ("- знание Flash", var_flash)
]
for text, var in skills:
    cb = tk.Checkbutton(frame_skills, text=text, variable=var,
                        bg="white", activebackground="white", anchor="w", relief="flat")
    cb.pack(anchor="w", padx=10, pady=1)

#Дополнительные сведения
lbl_extra = tk.Label(main_frame, text="Дополнительные сведения о себе",
                     font=("Arial", 10), bg="#e2debc", relief="solid", bd=1)
lbl_extra.grid(row=6, column=0, sticky="nsew", pady=0, padx=(0, 0))

frame_extra = tk.Frame(main_frame, bg="#d3d3d3", relief="solid", bd=1)
frame_extra.grid(row=6, column=1, sticky="ew", pady=0, padx=(0, 0))
text_additional = tk.Text(frame_extra, height=5, width=30, font=("Arial", 9),
                          bg="white", wrap=tk.WORD, relief="solid", bd=1)
text_additional.pack(side="left", padx=2, pady=2)

main_frame.columnconfigure(1, weight=1)

button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=15)

btn_register = tk.Button(button_frame, text="зарегистрировать",
                         command=submit_form, width=18,
                         bg="#8f8f8f", fg="white", font=("Arial", 10), bd=1)
btn_register.pack(side="left", padx=10)

btn_clear = tk.Button(button_frame, text="очистить форму",
                      command=clear_form, width=18,
                      bg="#8f8f8f", fg="white", font=("Arial", 10), bd=1)
btn_clear.pack(side="right", padx=10)

root.mainloop()