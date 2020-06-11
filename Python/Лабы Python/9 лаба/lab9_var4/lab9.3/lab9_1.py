# Импорт модулей
"""Комментарии в lab9.1"""
def StartApp(window):
    # Импорт модулей
    import tkinter as tk
    from PIL import ImageTk, Image
    from logic import Calculate


    # Инициализация окна
    root = tk.Toplevel(window) # Создаём дочернее окно от окна window
    root.geometry('400x500+770+260')
    root.resizable(False, False)
    root.configure(bg='#708090')

    # Функции определяющие поведение элементнов
    def Calc():
        label_3.configure(text='')
        data = Calculate()
        arg = str(data[0]).replace('[', '').replace(']', '')
        result = data[1]
        label_1.configure(text=arg)
        label_2.configure(text=result)

    def Save():
        label_3.configure(text='Сохранение прошло успешно!', fg='white')
        result = label_2.cget("text")
        file = open('out.txt', 'w') # Открываем файл в режиме записи (если данный файл не существует, то создаём новый)
        file.write(result) # Записываем в файл данные из переменной result
        file.close() # Закрываем файл



    # Создание элементов окна
    label_1 = tk.Label(root, text='Входные значения', bg='#708090', fg='white')
    label_2 = tk.Label(root, text='', bg='#708090')
    label_3 = tk.Label(root, text='', bg='#708090')
    img = ImageTk.PhotoImage(Image.open("data/function.png"), master=root) # Открываем изображение и помещаем его в переменную
    labelImg = tk.Label(root, image=img, bg='black')

    buttonStart = tk.Button(root, text='Посчитать', command=Calc, bg='black', fg='white')
    buttonSave = tk.Button(root, text='Сохранить', command=Save, bg='black', fg='white')

    # Размещение элементов
    label_1.place(y=40, x=155)
    labelImg.place(y=100, x=120)
    label_2.place(y=210, x=135)
    label_3.place(y=420, x=107)
    buttonStart.place(y=450, x=110)
    buttonSave.place(y=450, x=210)