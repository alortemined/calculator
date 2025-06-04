import tkinter as tk

# Основное окно
root = tk.Tk()
root.title('Калькулятор')
root.geometry("400x500")

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
                # Пробуем преобразовать текущее значение в число
                num = float(current)
                # Меняем знак и обновляем поле
                num = -num
                # Убираем .0 у целых чисел для красоты
                if num.is_integer():
                    num = int(num)
                entry.delete(0, tk.END)
                entry.insert(0, str(num))
            except ValueError:
                # Если текущее значение не число, ничего не делаем
                pass
    else:
        clear_press_count = 0
        entry.insert(tk.END, char)

# Кнопки с добавленной кнопкой ±
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('C', '⌫', '±')  # добавлена кнопка ±
]

# Рисуем кнопки
for r, row in enumerate(buttons, start=1):
    for c, char in enumerate(row):
        btn = tk.Button(root, text=char, font=('Arial', 18), fg='white', bg='black',
                        command=lambda ch=char: on_click(ch), padx=20, pady=20)
        btn.grid(row=r, column=c, sticky="nsew")

# Распределение веса по строкам и колонкам
for i in range(6):  # теперь 6 строк, т.к. добавлена строка с кнопкой ±
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Запуск
root.mainloop()
