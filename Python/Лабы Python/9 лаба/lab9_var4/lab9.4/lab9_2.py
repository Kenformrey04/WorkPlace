"""Коммантарии в lab9.2"""
# Импорт модулей

def StartApp(root):
    import tkinter as tk
    from logic2 import Calculate


    # Инициализация окна
    root = tk.Toplevel(root)
    root.geometry('400x170+550+450')
    root.resizable(False, False)
    root.configure(bg='#708090')

    # Функции описывающие поведение элементов
    def Calc():
        arg = inputField.get()
        arg = arg.split(',')
        try:
            result = f'Результат:\n\n{Calculate(int(arg[0]), int(arg[1]), int(arg[2]))}'
        except:
            labelResult.configure(text='Введены некорректные данные!', bg='#708090', fg='white')
        else:
            labelResult.configure(text=result, bg='#708090', fg='white')

    # Создание элементов окна
    label = tk.Label(root, text='Введите коэффициенты a, b, c (Запятые обязательны!):', bg='#708090', fg='white')
    labelResult = tk.Label(root, text='', bg='#708090')
    inputField = tk.Entry(root, width=10)
    buttonCalc = tk.Button(root, text='Вычислить', command=Calc, bg='black', fg='white')

    # Позиционирование элементов
    label.place(y=20, x=10)
    inputField.place(y=20, x=320)
    labelResult.place(y=60, x=150)
    buttonCalc.place(y=130, x=170)

    