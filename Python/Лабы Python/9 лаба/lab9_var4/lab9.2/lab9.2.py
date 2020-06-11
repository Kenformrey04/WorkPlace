# Импорт модулей
import tkinter as tk
from logic import Calculate


# Инициализация окна
root = tk.Tk() # Инициализация объекта класса TK
root.geometry('400x170+770+260') # Размер и смещение
root.resizable(False, False) # Фиксирование размеров окна
root.configure(bg='#708090') # Цвет

# Функции описывающие поведение элементов
def Calc(): # Функия после нажатия кнопки "Вычислить"
    arg = inputField.get() # Получаем данные из поля для ввода
    arg = arg.split(',') # Создаём список из строки по разделителю ','
    try: # Поиск и обработка исключений
        result = f'Результат:\n\n{Calculate(int(arg[0]), int(arg[1]), int(arg[2]))}' # Присваиваем результат вычисления функции Calculate() из модуля logic
    except: # Если возникло исключение
        labelResult.configure(text='Введены некорректные данные!', bg='#708090', fg='white') # Изменяем текст, цвет фона, цвет текста надписи
    else: # Если код отработал без исключений
        labelResult.configure(text=result, bg='#708090', fg='white') # Изменяем текст, цвет фона, цвет текста надписи

# Создание элементов окна
label = tk.Label(root, text='Введите коэффициенты a, b, c (Запятые обязательны!):', bg='#708090', fg='white') # Надпись
labelResult = tk.Label(root, text='', bg='#708090') # Надпись для вывода результата
inputField = tk.Entry(root, width=10) # Поле для ввода данных
buttonCalc = tk.Button(root, text='Вычислить', command=Calc, bg='black', fg='white') # Кнопка "Вычислить", команда при нажатии - Calc()

# Позиционирование элементов
label.place(y=20, x=10)
inputField.place(y=20, x=320)
labelResult.place(y=60, x=150)
buttonCalc.place(y=130, x=170)

# Запуск безконечного цикла приложения
root.mainloop()