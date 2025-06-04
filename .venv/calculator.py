import tkinter as tk
import math

# Основное окно
root = tk.Tk()
root.title('Калькулятор')
root.geometry("400x550")  # немного увеличена высота для новой кнопки

# Поле ввода
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

clear_press_count = 0

def on_click(char):
    global clear_press_count

    if char == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
            clear_press_count = 0
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Ошибка")
            clear_press_count = 0
    elif char == 'C':
        clear_press_count += 1
        if clear_press_count == 1:
            entry.delete(0, tk.END)
        elif clear_press_count == 2:
            entry.delete(0, tk.END)
            entry.insert(0, "Полный сброс!")
            clear_press_count = 0
    elif char == '⌫':
        clear_press_count = 0
        entry.delete(len(entry.get()) - 1, tk.END)
    elif char == '±':
        clear_press_count = 0
        current = entry.get()
        if current:
            try:
                num = float(current)
                num = -num
                if num.is_integer():
                    num = int(num)
                entry.delete(0, tk.END)
                entry.insert(0, str(num))
            except ValueError:
                pass
    elif char == '√':
        clear_press_count = 0
        current = entry.get()
        if current:
            try:
                num = float(current)
                if num < 0:
                    entry.delete(0, tk.END)
                    entry.insert(0, "Ошибка")
                else:
                    result = math.sqrt(num)
                    if result.is_integer():
                        result = int(result)
                    entry.delete(0, tk.END)
                    entry.insert(0, str(result))
            except ValueError:
                entry.delete(0, tk.END)
                entry.insert(0, "Ошибка")
    elif char == 'x²':
        clear_press_count = 0
        current = entry.get()
        if current:
            try:
                num = float(current)
                result = num ** 2
                if result.is_integer():
                    result = int(result)
                entry.delete(0, tk.END)
                entry.insert(0, str(result))
            except ValueError:
                entry.delete(0, tk.END)
                entry.insert(0, "Ошибка")
    else:
        clear_press_count = 0
        entry.insert(tk.END, char)

# Кнопки с добавленными ±, √ и x²
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('C', '⌫', '±', '√'),
    ('x²',)  # новая кнопка в отдельной строке
]

# Рисуем кнопки
for r, row in enumerate(buttons, start=1):
    for c, char in enumerate(row):

        btn = tk.Button(root, text=char, font=('Arial', 18), fg='grey', bg='green',

                        command=lambda ch=char: on_click(ch), padx=20, pady=20)
        btn.grid(row=r, column=c, sticky="nsew")

# Распределение веса по строкам и колонкам
for i in range(len(buttons) + 1):  # количество строк с учётом новой
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Запуск cr
root.mainloop()
