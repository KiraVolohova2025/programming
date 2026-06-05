#создать словарь из списков keys = ['Ten', 'Twenty', 'Thrity']
# и values =[10, 20, 30] 
import tkinter as tk
from tkinter import messagebox
from functools import reduce

# Исходные данные
keys, values = ['Ten', 'Twenty', 'Thirty'], [10, 20, 30]

# Функциональные операци
create_dict = lambda k, v: dict(zip(k, v))
dict_str = lambda d: '\n'.join(map(lambda i: f'  {i[0]} → {i[1]}', d.items()))
sum_vals = lambda d: reduce(lambda a, i: a + i[1], d.items(), 0)
map_vals = lambda d, f: dict(map(lambda i: (i[0], f(i[1])), d.items()))
filter_vals = lambda d, p: dict(filter(lambda i: p(i[1]), d.items()))

# GUI
root = tk.Tk()
root.title("Словарь")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

d = create_dict(keys, values)

def update():
    t.delete(1.0, tk.END)
    t.insert(1.0, f"{{\n{dict_str(d)}\n}}")
    stats.config(text=f"Сумма: {sum_vals(d)} | Кол-во: {len(d)}")

def op(f, v=None):
    global d
    d = map_vals(d, lambda x: x + v) if v else filter_vals(d, lambda x: x > 15)
    update()

def reset():
    global d
    d = create_dict(keys, values)
    update()

# Виджеты
tk.Label(root, text="Словарь из списков", font=("Arial",12,"bold"), bg="#f0f0f0").pack(pady=10)
tk.Label(root, text=f"keys = {keys}\nvalues = {values}", font=("Courier",9), bg="#f0f0f0").pack()
t = tk.Text(root, height=6, font=("Courier",10))
t.pack(pady=10, padx=20, fill=tk.X)
stats = tk.Label(root, text="", font=("Arial",10), bg="#f0f0f0")
stats.pack()

# Кнопки (функционально создала через map)
list(map(lambda btn: btn[0].pack(side=tk.LEFT, padx=4),
    [(tk.Button(root, text="+5", command=lambda: op('map',5), bg="#e2debc", width=8),),
     (tk.Button(root, text="×2", command=lambda: op('map', lambda x: x*2), bg="#e2debc", width=8),),
     (tk.Button(root, text=">15", command=lambda: op('filter'), bg="#e2debc", width=8),),
     (tk.Button(root, text="Сброс", command=reset, bg="#e2debc", width=8),)]))

# Фрейм для кнопок
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)
for btn in btn_frame.pack_slaves():
    btn.pack_forget()
    
tk.Button(root, text="+5", command=lambda: op('map',5), bg="#e2debc", width=10).pack(side=tk.LEFT, padx=5, pady=10)
tk.Button(root, text="×2", command=lambda: op('map', lambda x: x*2), bg="#e2debc", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(root, text=">15", command=lambda: op('filter'), bg="#e2debc", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(root, text="Сброс", command=reset, bg="#e2debc", width=10).pack(side=tk.LEFT, padx=5)

update()
root.mainloop()