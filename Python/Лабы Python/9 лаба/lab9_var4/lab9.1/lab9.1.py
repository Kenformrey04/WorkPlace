# Импорт модулей
import tkinter as tk
from PIL import ImageTk, Image
from logic import Calculate


# Инициализация окна
root = tk.Tk() # Создаём экземпляр класса Tk
root.geometry('400x500+770+260') # Устанавливаем размер окна и его смешение (+770 - горизонтально вправо, +260 - вертикально вниз)
root.resizable(False, False) # Устанавливаем запрет на изменение размеров окна
root.configure(bg='#708090') # Устанавливаем цвет

# Функции определяющие поведение элементнов
def Calc(): # Функция при нажатии на кнопку "Посчитать"
    label_3.configure(text='') # Изменяем текст надписи
    data = Calculate() # Вызываем функцию Calculate() из модуля logic и присваеваем возвращаемое значение - кортеж из (аргументов, результата вычислений) - переменной data
    arg = str(data[0]).replace('[', '').replace(']', '') # Присваиваем в переменную аргументы, преобразовав данные в строку и удалив лишние символы
    result = data[1] # Присваиваем в переменную результат
    label_1.configure(text=arg) # Изменяем текст надписи
    label_2.configure(text=result) # Изменяем текст надписи

def Save(): # Функция при нажатии на кнопку "Сохранить"
        label_3.configure(text='Сохранение прошло успешно!', fg='white') # Изменяем текст надписи и цвет текста
        result = label_2.cget("text") # Получаем текст из надписи 
        file = open('out.txt', 'w') # Открываем файл в режиме записи (если данный файл не существует, то создаём новый)
        file.write(result) # Записываем в файл данные из переменной result
        file.close() # Закрываем файл



# Создание элементов окна
label_1 = tk.Label(root, text='Входные значения', bg='#708090', fg='white') # Создаём надпись
label_2 = tk.Label(root, text='', bg='#708090') # Создаём надпись
label_3 = tk.Label(root, text='', bg='#708090') # Создаём надпись
img = ImageTk.PhotoImage(Image.open("data/function.png"), master=root) # Открываем изображение и помещаем его в переменную
labelImg = tk.Label(root, image=img, bg='black') # Создаём надпись и помещаем в неё изображение

buttonStart = tk.Button(root, text='Посчитать', command=Calc, bg='black', fg='white') # Создаём кнопку. Функция при нажатии - Calc()
buttonSave = tk.Button(root, text='Сохранить', command=Save, bg='black', fg='white') # Создаём кнопку. Функция при нажатии - Save()

# Размещение элементов с помощью метода place(y=координата по оси y, x=координата по оси x)
label_1.place(y=40, x=155) 
labelImg.place(y=100, x=120)
label_2.place(y=210, x=135)
label_3.place(y=420, x=107)
buttonStart.place(y=450, x=110)
buttonSave.place(y=450, x=210)

# Запуск безконечного цикла, который завершится в случае закрытия окна
root.mainloop()