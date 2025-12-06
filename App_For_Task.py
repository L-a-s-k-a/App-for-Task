import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_task():
    # Получаем дату из поля ввода
    birth_date_str = entry.get().strip()
    
    # Если в поле только подсказка, выходим
    if birth_date_str == "дд.мм.гггг" or not birth_date_str:
        messagebox.showwarning("Предупреждение", "Пожалуйста, введите дату рождения")
        clear_all()
        return

    try:
        # Парсим дату (ожидаем формат ДД.ММ.ГГГГ)
        birth = datetime.strptime(birth_date_str, "%d.%m.%Y")
        today = datetime.now()
        
        # Вычисляем сумму дня и месяца
        task_calculate = birth.day + birth.month
        
        # Вычисляем двоичное чилсо по дате рождения
        bin_calculate = str(birth.day) + str(birth.month) + str(birth.year)
        bin_check = format(int(bin_calculate), '032b')
        
        # Корректируем возраст, если день рождения еще не наступил в этом году
        if (birth.year > today.year    or 
            (birth.year == today.year and birth.month > today.month) or
            (birth.year == today.year and birth.month == today.month and birth.day > today.day)):
            error_date = True    
            messagebox.showwarning("Предупреждение", "Похоже, вы ещё не родились\n" "Пожалуйста, введите корректную дату рождения")
            task_calculate = 0
            bin_calculate = 0
            bin_check = 0
            clear_all()
        elif (today.year - birth.year) > 110:
            error_date = True
            messagebox.showwarning("Предупреждение", "Похоже, вы умерли\n" "Пожалуйста, введите корректный год")
            task_calculate = 0
            bin_calculate = 0
            bin_check = 0
            clear_all()
     
        # truth_table = None
                    
        # Определяем задание в зависимости от возраста
        if 1 <= task_calculate <= 15:
            error_date = False   
            truth_table = "Запись числа в таблицу истинности происходит слева направо\n"
            if (task_calculate % 2) != 1:
                truth_table += "Все задания выполняются в базисе 3И-НЕ\n"
            else:
                truth_table += "Все задания выполняются в базисе 4ИЛИ-НЕ\n"
            
            if (int(task_calculate / 3) % 2) == 1:
                truth_table += "Микросхема дешифратора К155ИД4\n"
                truth_table += "Микросхема мультиплексора К155КП7"
            elif (int(task_calculate / 2) % 2) == 0:
                truth_table += "Микросхема дешифратора К155ИД3\n"
                truth_table += "Микросхема мультиплексора К155КП2"
            elif (int(task_calculate / 2) % 2) == 1:
                truth_table += "Микросхема дешифратора К155ИД10\n"
                truth_table += "Микросхема мультиплексора К155КП1"
            else:
                truth_table += "Микросхема дешифратора К155ИД1\n"
                truth_table += "Микросхема мультиплексора К155КП5"
        
        elif 16 <= task_calculate <= 25:
            error_date = False
            truth_table = "Запись числа в таблицу истинности происходит справа налево\n"
            if (task_calculate % 2) != 1:
                truth_table += "Все задания выполняются в базисе 2ИЛИ-НЕ\n"
            else:
                truth_table += "Все задания выполняются в базисе 3И-НЕ\n"
                
            if (int(task_calculate / 3) % 2) == 1:
                truth_table += "Микросхема дешифратора К155ИД10\n"
                truth_table += "Микросхема мультиплексора К155КП5"
            elif (int(task_calculate / 2) % 2) == 0:
                truth_table += "Микросхема дешифратора К155ИД1\n"
                truth_table += "Микросхема мультиплексора К155КП7"
            elif (int(task_calculate / 2) % 2) == 1:
                truth_table += "Микросхема дешифратора К155ИД4\n"
                truth_table += "Микросхема мультиплексора К155КП2"
            else:
                truth_table += "Микросхема дешифратора К155ИД3\n"
                truth_table += "Микросхема мультиплексора К155КП1"
        
        elif 26 <= task_calculate <= 37:
            error_date = False
            truth_table = "Запись числа в таблицу истинности происходит слева направо\n"
            if (task_calculate % 2) != 1:
                truth_table += "Все задания выполняются в базисе 4ИЛИ-НЕ\n"
            else:
                truth_table += "Все задания выполняются в базисе 2И-НЕ\n"
                
            if (int(task_calculate / 3) % 2) == 1:
                truth_table += "Микросхема дешифратора К155ИД3\n"
                truth_table += "Микросхема мультиплексора К155КП5"
            elif (int(task_calculate / 2) % 2) == 0:
                truth_table += "Микросхема дешифратора К155ИД10\n"
                truth_table += "Микросхема мультиплексора К155КП7"
            elif (int(task_calculate / 2) % 2) == 1:
                truth_table += "Микросхема дешифратора К155ИД1\n"
                truth_table += "Микросхема мультиплексора К155КП2"
            else:
                truth_table += "Микросхема дешифратора К155ИД4\n"
                truth_table += "Микросхема мультиплексора К155КП1"
        
        elif task_calculate >= 38:
            error_date = False
            truth_table = "Запись числа в таблицу истинности происходит справа налево\n"
            if (task_calculate % 2) != 1:
                truth_table += "Все задания выполняются в базисе 4И-НЕ\n"
            else:
                truth_table += "Все задания выполняются в базисе 3ИЛИ-НЕ\n"
            
            if (int(task_calculate / 3) % 2) == 1:
                truth_table += "Микросхема дешифратора К155ИД1\n"
                truth_table += "Микросхема мультиплексора К155КП1"
            elif (int(task_calculate / 2) % 2) == 0:
                truth_table += "Микросхема дешифратора К155ИД4\n"
                truth_table += "Микросхема мультиплексора К155КП5"
            elif (int(task_calculate / 2) % 2) == 1:
                truth_table += "Микросхема дешифратора К155ИД3\n"
                truth_table += "Микросхема мультиплексора К155КП7"
            else:
                truth_table += "Микросхема дешифратора К155ИД10\n"
                truth_table += "Микросхема мультиплексора К155КП2"
        
        if error_date != True:    
            # Обновляем поле с результатом
            result_text_widget.config(state='normal', fg='black')
            # result_text_widget.config(fg='black')  # Возвращаем обычный цвет текста
            result_text_widget.delete(1.0, tk.END)
            result_text_widget.insert(1.0, truth_table)
            result_text_widget.tag_add("center", "1.0", "end") # Применяем тег центрирования ко всему тексту
            result_text_widget.config(state='disabled')
            
            # Обновляем поле с двоичным результатом
            binar_text_widget.config(state='normal', fg='black')
            # binar_text_widget.config(fg='black')  # Возвращаем обычный цвет текста
            binar_text_widget.delete(1.0, tk.END)
            binar_text_widget.insert(1.0, (str(bin_calculate) + " = " + str(bin_check)))
            binar_text_widget.tag_add("center", "1.0", "end") # Применяем тег центрирования ко всему тексту
            binar_text_widget.config(state='disabled')
        print(task_calculate % 2)
        print(int(task_calculate / 3) % 2)
        print(int(task_calculate / 2) % 2)
    
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите дату в формате ДД.ММ.ГГГГ\nНапример: 12.08.2001")
        clear_all()
        
# Функция очищает поле ввода и устанавливает фокус на него
def clear_input():
    entry.delete(0, tk.END)
    entry.focus()

# Функция очищает поле ввода и поле результата
def clear_all():
    entry.delete(0, tk.END)
    result_text_widget.config(state='normal', fg='grey')
    result_text_widget.delete(1.0, tk.END)
    result_text_widget.insert(1.0, "Здесь будет вариант задания")
    result_text_widget.tag_add("center", "1.0", "end")
    result_text_widget.config(state='disabled')
    
    binar_text_widget.config(state='normal', fg='grey')
    binar_text_widget.clipboard_clear()
    binar_text_widget.delete(1.0, tk.END)
    binar_text_widget.insert(1.0, "Здесь будет сформированное 32-х разрядное двоичное число")
    binar_text_widget.tag_add("center", "1.0", "end")
    binar_text_widget.config(state='disabled')
    entry.focus()

# Функция обрабатывает нажатие Enter
def on_enter_key(event):
    calculate_task()

# Функция обработывает нажатие Escape - производит очистку поля ввода
def on_escape_key(event):
    clear_input()

# Функция обрабатывает получение фокуса - производит удаление подсказки
def on_focusin(event):
    if entry.get() == "дд.мм.гггг":
        entry.delete(0, tk.END)
        entry.config(fg='black')  # Возвращаем обычный цвет текста

# Функция обработывает потерю фокуса - производит добавление подсказки, если поле пустое
def on_focusout(event):
    if entry.get() == "":
        entry.insert(0, "дд.мм.гггг")
        entry.config(fg='grey')  # Серый цвет для подсказки

# Создание и настройка главного окна
root = tk.Tk()
root.title("Генератор вариантов индивидуального домашнего задания")
try:
    # Создаем пустое прозрачное изображение минимального размера
    transparent_icon = tk.PhotoImage(width=1, height=1)
    # Устанавливаем его как иконку
    root.iconphoto(True, transparent_icon)
except tk.TclError:
    pass # Или можно оставить print
root.geometry("655x460")  # Увеличили высоту для новой кнопки
root.resizable(False, False)

# Настраиваем стиль
root.configure(bg='#f0f0f0')
font_style = ("Cambria", 14, "bold")

# Создаем главный фрейм с возможностью изменения размера
main_frame = tk.Frame(root, bg='#f0f0f0', width=655)
main_frame.pack(side='left', fill='both', expand=False)
main_frame.pack_propagate(False)  # Запрещаем изменение размера фрейма

# Заголовок
title_label = tk.Label(
    main_frame, 
    text="Введите вашу дату рождения", 
    font=("Cambria", 16, "bold"),
    bg='#f0f0f0',
    fg='#333333'
)
title_label.pack(pady=10)

# Подсказка по формату
format_label = tk.Label(
    main_frame,
    text="Формат: ДД.ММ.ГГГГ (например: 12.08.2001)",
    font=("Cambria", 12),
    bg='#f0f0f0',
    fg='#666666'
)
format_label.pack(pady=5)

# Поле для ввода даты
entry_frame = tk.Frame(main_frame, bg='#f0f0f0')
entry_frame.pack(pady=15)

entry = tk.Entry(
    entry_frame,
    font=("Cambria", 14),
    width=15,
    justify='center'
)
entry.pack(padx=10)

# Привязываем обработчики событий
entry.bind("<FocusIn>", on_focusin)
entry.bind("<FocusOut>", on_focusout)
entry.bind("<Return>", on_enter_key)
entry.bind("<Escape>", on_escape_key)  # Очистка по Escape
entry.focus()

# Устанавливаем начальную подсказку
entry.insert(0, "дд.мм.гггг")

# Фрейм для кнопок
button_frame = tk.Frame(main_frame, bg='#f0f0f0')
button_frame.pack(pady=15)

# Кнопка расчета
calculate_button = tk.Button(
    button_frame,
    text="Рассчитать вариант",
    font=font_style,
    command=calculate_task,
    bg='#4CAF50',
    fg='white',
    padx=20,
    pady=10,
    cursor='hand2'
)
calculate_button.pack(side='left', padx=5)

# Кнопка очистки поля ввода
clear_input_button = tk.Button(
    button_frame,
    text="Очистить поле",
    font=font_style,
    command=clear_input,
    bg='#ff9800',
    fg='white',
    padx=20,
    pady=10,
    cursor='hand2'
)
clear_input_button.pack(side='left', padx=5)

# Кнопка очистки всего
clear_all_button = tk.Button(
    button_frame,
    text="Очистить всё",
    font=font_style,
    command=clear_all,
    bg='#f44336',
    fg='white',
    padx=20,
    pady=10,
    cursor='hand2'
)
clear_all_button.pack(side='left', padx=5)

# Поле для вывода двоичного числа
result_binar_frame = tk.Frame(main_frame, bg='#ffffff', relief='solid', bd=1)
result_binar_frame.pack(pady=10, padx=10, fill='both', expand=False)

binar_text_widget = tk.Text(
    result_binar_frame,
    font=("Cambria", 14),
    bg='#ffffff',
    fg='#333333',
    wrap='word',  # Перенос по словам
    padx=10,
    pady=10,
    state='disabled',
    height=1
)
binar_text_widget.pack(fill='both', expand=False)

# Создаем тег для центрирования текста
binar_text_widget.tag_configure("center", justify='center')

# Вставляем начальный текст с центрированием
binar_text_widget.config(state='normal', fg='grey')
binar_text_widget.insert(1.0, "Здесь будет сформированное 32-х разрядное двоичное число")
binar_text_widget.tag_add("center", "1.0", "end")
binar_text_widget.config(state='disabled', width=655)

# Поле для вывода результата с прокруткой
result_frame = tk.Frame(main_frame, bg='#ffffff', relief='solid', bd=1)
result_frame.pack(fill='both', expand=False, pady = 10, padx = 10)

# Текстовый виджета
result_text_widget = tk.Text(
    result_frame,
    font=("Cambria", 14),
    bg='#ffffff',
    fg='#333333',
    wrap='word',  # Перенос по словам
    padx=10,
    pady=10,
    state='disabled',
    height=4
)
result_text_widget.pack(fill='both', expand=True)

# Создаем тег для центрирования текста
result_text_widget.tag_configure("center", justify='center')

# Вставляем начальный текст с центрированием
result_text_widget.config(state='normal', fg='grey')
result_text_widget.insert(1.0, "Здесь будет вариант задания")
result_text_widget.tag_add("center", "1.0", "end")
result_text_widget.config(state='disabled', width=655)

# Добавляем подсказку в статусную строку
status_label = tk.Label(
    main_frame,
    text="Подсказка: Enter - расчет, Escape - очистка поля, кнопки для других действий",
    font=("Cambria", 11),
    bg='#e0e0e0',
    fg='#666666',
    pady=5
)
status_label.pack(side='bottom', fill='x')

# Настройка весов для адаптивного изменения размера
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(7, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Запускаем главный цикл
root.mainloop()