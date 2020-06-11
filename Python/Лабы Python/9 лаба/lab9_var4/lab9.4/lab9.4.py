# Импорт модулей
from lab9_1 import StartApp as StartApp1
from lab9_2 import StartApp as StartApp2
from tkinter import *
from PIL import ImageTk, Image




# Создаём окно
root = Tk() # Инициализируем окно
root.geometry('200x130+750+300') # Установка размеров окна (400x400) и положения окна на мониторе (+750+300)
# root.resizable(False, False) # Устанавливаем невозможность изменения размеров окна

# Функции для элементов окна

img = ImageTk.PhotoImage(Image.open("data/function.png")) # Открываем изображение и помещаем его в переменную

def clicked(): # Функция срабатывает после нажатия на кнопку
    selected = select_1.get() + select_2.get()

    if selected == 1: # Условие: Если значение переключателя = 1
        StartApp1(root, img) # Запускаем приложение из lab9_1.py
    elif selected == 2: # Условие: Если значение переключателя = 2
        StartApp2(root) # Запускаем приложение из lab9_2.py
    elif selected == 3:
        StartApp1(root, img)
        StartApp2(root)


# Создаём элементы окна

# Создаём области окна (фреймы)
top_frame = Frame(root) # Верхний фрейм
bottom_frame = Frame(root) # Нижний фрейм

select_1 = IntVar() # Присваиваем переменной объект класса, который ожидает присваивания значения (целочисленного)
select_2 = IntVar()

# Переключательи
radioButton_1 = Checkbutton(top_frame, text="Расчёт значений", onvalue=1, offvalue=0, variable=select_1, pady=5) # Создаём переключатель, помещаем в врехний фрейм, устанавливаем текст, присваиваем значение переключателю 1.
radioButton_2 = Checkbutton(bottom_frame, text="Проверка года   ", onvalue=2, offvalue=0, variable=select_2, pady=5) # Создаём переключатель, помещаем в врехний фрейм, устанавливаем текст, присваиваем значение переключателю 2.

# Кнопки
button = Button(bottom_frame, text='Ок', width=10, command=clicked) # Создаём кнопку и помещаем в нижний фрейм, устанавливаем текст, ширину. По нажатию кнопки будет выполнятся функция clicked()

# Размещение объектов в окне (размещаем фреймы и элементы функцией pack())

#фреймы
top_frame.pack() # Размещаем верхний фрейм
bottom_frame.pack(pady=7) # Размещаем нижний фрейм с отступов сверху и снизу 7

#элементы
radioButton_1.pack() # Размещаем переключатель
radioButton_2.pack(side=TOP) # Размещаем переключатель и прижимаем его к низу
button.pack(side=BOTTOM, pady=13) # Размещаем кнопку, прижимаем её к низу, устанавливаем отступ сверху и снизу 13

# Запуск приложения
root.mainloop() # Вызываем бесконечный цикл приложения (его окончание будет следовать закрытию окна)