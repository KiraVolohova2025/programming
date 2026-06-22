"""
Создать словарь из списков
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
"""
import tkinter as tk
from tkinter import messagebox

def create_dictionary():
    try:
        # Получаем текст из полей ввода
        keys_text = entry_keys.get().strip()
        values_text = entry_values.get().strip()
        
        #Проверка на пустые поля
        if not keys_text or not values_text:
            messagebox.showerror("Ошибка", "Заполните оба поля!")
            return
        # Преобразуе строки в списки
        keys = [item.strip() for item in keys_text.split(',')]
        values = [int(item.strip()) for item in values_text.split(',')]
        
        # Проверка на одинаковую длину списков
        if len(keys) != len(values):
            messagebox.showerror("Ошибка", 
                                 f"Количество ключей ({len(keys)}) не совпадает с количеством значений ({len(values)})!")
            return
    
        # Создаём словарь
        dictionary = dict(zip(keys, values))
        # Формируем текст для вывода
        result_text = "Исходные данные:\n"
        result_text += f"keys   = {keys}\n"
        result_text += f"values = {values}\n\n"
        result_text += "Созданный словарь:\n"
        for k, v in dictionary.items():
            result_text += f"  {k} -> {v}\n"
        result_text += f"\nПолный словарь: {dictionary}"
        
        label_result.config(text=result_text, fg="green")
    except ValueError:
        messagebox.showerror("Ошибка", "Значения должны быть числами!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


def load_example():
    entry_keys.delete(0, tk.END)
    entry_values.delete(0, tk.END)
    entry_keys.insert(0, "Ten, Twenty, Thirty")
    entry_values.insert(0, "10, 20, 30")


def clear_all():
    entry_keys.delete(0, tk.END)
    entry_values.delete(0, tk.END)
    label_result.config(text="", fg="green")


root = tk.Tk()
root.title("Создание словаря из списков")
root.geometry("550x500")
root.configure(bg="#f0f0f0")
root.resizable(False, False)
# Заголовок
tk.Label(
    root,
    text="Создание словаря из списков",
    font=("Arial", 14, "bold"),
    bg="#f0f0f0",
    fg="#333"
).pack(pady=15)
# Рамка для ввода данных
frame_input = tk.LabelFrame(root, text="Ввод данных", font=("Arial", 10, "bold"),
                             bg="#f0f0f0", fg="#333", padx=10, pady=10)
frame_input.pack(padx=20, pady=10, fill="x")
# Поле для ввода ключей
tk.Label(frame_input, text="Ключи (через запятую):", 
         bg="#f0f0f0", anchor="w").pack(fill="x", pady=(5,0))
entry_keys = tk.Entry(frame_input, font=("Arial", 10), width=50)
entry_keys.pack(fill="x", pady=(0, 10))
tk.Label(frame_input, text="Пример: Ten, Twenty, Thirty", 
         bg="#f0f0f0", fg="gray", font=("Arial", 8)).pack(anchor="w", pady=(0,5))
# Поле для ввода значений
tk.Label(frame_input, text="Значения (через запятую):", 
         bg="#f0f0f0", anchor="w").pack(fill="x", pady=(5,0))
entry_values = tk.Entry(frame_input, font=("Arial", 10), width=50)
entry_values.pack(fill="x", pady=(0, 10))
tk.Label(frame_input, text="Пример: 10, 20, 30", 
         bg="#f0f0f0", fg="gray", font=("Arial", 8)).pack(anchor="w")
# Кнопки управления
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Создать словарь",
    command=create_dictionary,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    width=14,
    relief="flat"
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Пример",
    command=load_example,
    bg="#2196F3",
    fg="white",
    font=("Arial", 10, "bold"),
    width=14,
    relief="flat"
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Очистить всё",
    command=clear_all,
    bg="#f44336",
    fg="white",
    font=("Arial", 10, "bold"),
    width=14,
    relief="flat"
).pack(side="right", padx=5)

frame_output = tk.LabelFrame(root, text="Результат", font=("Arial", 10, "bold"),
                              bg="#f0f0f0", fg="#333", padx=10, pady=10)
frame_output.pack(padx=20, pady=10, fill="both", expand=True)
# Метка для вывода результата
label_result = tk.Label(
    frame_output,
    text="",
    font=("Courier", 10),
    bg="#f0f0f0",
    fg="green",
    justify="left",
    wraplength=480
)
label_result.pack(fill="both", expand=True)

root.mainloop()