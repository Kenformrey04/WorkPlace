# Импорт модулей
from tkinter import *

def StartApp(): # Функция запукающая приложение
    # Создаём окно
    root = Tk() # Инициализируем окно
    root.geometry('700x530+585+230') # Установка размеров окна (400x400) и положения окна на мониторе (+750+300)
    root.minsize(width=462, height=341) # Минимальные ширина и высота
    root.configure(bg='#778899') # Цвет окна
    root.title("Холст") # Надпись на рамке окна
    
    top_frame = Frame(root, borderwidth=0.5, relief=GROOVE) # Создаём верхний фрейм (в окне, ширина границ, рельеф)
    bot_frame = Frame(root, bg='#778899') # Нижний фрейм (цвет)

    def PaintTriangle(event): # Фунция рисущая треугольник
        point_x = canvas.canvasx(event.x, gridspacing=None) # Получаем координату курсора по оси x
        point_y = canvas.canvasy(event.y, gridspacing=None) # Получаем координату курсора по оси y
        canvas.create_polygon([point_x, point_y - 40],[point_x + 40, point_y + 40],[point_x - 40, point_y + 40],fill="#00FF00", outline="#ff0000", tags='triangle', width=0) # Создаём полигон

    def PaintBorderTriangle(event): # Функция, изменяющая границы выбранного треугольника
        point_x = canvas.canvasx(event.x, gridspacing=None) # Получаем координату курсора по оси x
        point_y = canvas.canvasy(event.y, gridspacing=None) # Получаем координату курсора по оси y

        items = [] #  Список для хранения ID найденных элементов
        counter = 0 # Счётчик для корректного поиска верного треугольника

        # Выполнаяем поиск элемента в указанной области
        item = canvas.find_overlapping(point_x, point_y, point_x, point_y - 81) # Поиск элемента по вертикальной линии вверх
        for i in item: # Цикл для добавления элемента в список
            items.append(i) # Добавляем элемент в список (если ничего не найдено, то ничего не попадает в список)
        item = canvas.find_overlapping(point_x, point_y, point_x + 81, point_y) # По горизонтальной линии вправо
        for i in item: # 
            items.append(i) #
        item = canvas.find_overlapping(point_x, point_y, point_x, point_y + 81) # По вертикальной линии вниз
        for i in item: #
            items.append(i) #
        item = canvas.find_overlapping(point_x, point_y, point_x - 81, point_y) # По горизонтальной линии влево
        for i in item: #
            items.append(i) #

        max = 0 # Переменная для определения максимального количества совпадений определённого элемента в списке элементов
        elemetn = -1 # Объявляем переменную для хранения элементов. Инициализируем -1. -1 будет означать, что ни одного элемента не было найдено
        for i in items: # Цикл для прохода по списку найденных элементов (если их нет, то цикл не выполнится)
            if items.count(i) >= max: # Условие: Если элемент списка i встречается в списке больше раз, чем предыдущий, либо столько же, то выполняем.
#(>= стоит для того, чтобы программа работала корректно при наложении одного треугольника на другой. Эксперементально выявленно, что последнее совпадение относится к нужному треугольнику)
                max = items.count(i) # Добавляем количество совпадений элемента i в списке items как новое максимальное число совпадений
                elemetn = i # Перезаписываем элемент

        if max == 4: # Если число максимальных совпадений элемента равно 4 (именно столько нужно, так как мы должны убедиться, что курсор находится внутри элемента )
            canvas.itemconfig(elemetn, width=2) # Изменяем конфигурацию найденного элемента (Увеличиваем толщину границ полигона, чем и является наш треугольник)

    def ClearCanvas(): # Функиця, очищающая холст
        items = canvas.find_withtag("triangle") # Находим все элементы с тегом "triangle"
        for i in items: # Цикл для прохода по списку найденных элементов
            canvas.delete(i) # Удаляем элемент с ID i-того элемента

    # Создаём элементы
    canvas = Canvas(top_frame, bg='white') # Создаём холст в верхнем фрейме
    button = Button(bot_frame, text='Очистить', width=10, command=ClearCanvas) # Кнопка "Очистить" в нижнем фрейме. Команда при нажатии - ClearCanvas 

    # Размещаем элементы и фреймы
    #Фреймы
    top_frame.pack(expand=True, fill=BOTH, pady=20, padx=10) # Размещаем фрейм (expand=True - элемент будет заполнять всё пространство блока,
# fill - растяжение элемента при изменении размеров окна = BOTH - элемент будет растягиваться по вертикали и горизонтали, заполняя всё доступное пространство)
    bot_frame.pack(side=BOTTOM) # Размещаем нижний фрейм, прижимая его к низу
    #Элементы
    canvas.pack(expand=True, fill=BOTH) # Размещаем холст аналогично верхнему фрейму
    button.pack(pady=10) # Размещаем кнопку (отступ сверху и снизу 10)


    # Свойства при нажатии на мышь
    canvas.bind('<Double-1>', PaintTriangle) # При двойном клике ЛКМ по холсту выполняем функцию PaintTriangle
    canvas.bind('<Double-3>', PaintBorderTriangle) # При двойном клике ПКМ по холсту выполняем функцию PaintBorderTriangle

    root.mainloop() # Запускаем бесконечный цикл окна. Он прервётся в случае уничтожения окна


StartApp() # Запускаем приложение