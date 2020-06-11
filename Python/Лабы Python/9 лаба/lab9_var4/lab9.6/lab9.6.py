# Импорт модулей
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile


root = Tk() # Создаём окно
root.geometry('800x600+550+200') # Размеры и смещение
root.configure(bg='#778899') # Цвет окна
root.minsize(width=900, height=600) # Минимальные размеры

top_frame = Frame(root, bg='gray') # Верхний фрейм
bot_frame = Frame(root, bg='blue') # Нижний фрейм

# Функции элементов
def OpenFile(): # Функция, открываюшая файл в диалоговом окне
    textEdit.configure(state='normal') # Вкл редактирование
    textEdit.delete('1.0', END) # Удаляем весь текст из текстового поля
    filename =  askopenfile(initialdir="test/", mode='r', filetypes=[("Text files","*.txt"),("all files","*.*")]) # Открываем файл в режиме чтения
#initialdir - начальная директориа, в которой открывается диалоговое окно, filetypes - указываем отображаемые файлы с определёнными типами (текстовые файлы, все файлы). 
    file = str(filename.read()) # Считываем информацию из файла и преобразовываем информацию в тип str (строка)
    textEdit.insert('1.0', file) # Вставляем информацию из файла в текстовое поле (вначало, index='1.0')
    filename.close() # Закрываем файл

def SaveFile(): # Функция сохраняющая файл в режиме диалогового окна
    data = textEdit.get('1.0', END) # Получаем информацию из текстового поля (от начала и до конца, index1='1.0', index2='END') и записываем в переменную 
    filename = asksaveasfile(initialdir='test/', filetypes=[("Text files","*.txt"),("all files","*.*")], defaultextension=".txt") # Открываем диалоговое окно, defaultextension - тип файла по умолчанию (у нас это txt)
    filename.write(data) # Записываем данные в файл
    filename.close() # Закрываем файл
        
def ExitProgramm(): # Функция для выхода из программы
    dialog = Toplevel(root) # Создаём дочернее диалоговое окно
    dialog.geometry('200x80+850+450') # Размеры и смещение
    dialog.resizable(False, False) # Запрет на изменение размера окна

    Top_frame = Frame(dialog) # Верхний фрейм
    Bot_frame = Frame(dialog) # Нижний фрейм

    label = Label(Top_frame, text='Сохранить файл перед выходом?') # Надпись в верхнем фрейме

    def SaveAndExit(): # Функция сохраняющая файл перед выходом из программы
        try: # Отлавливаем исключения (код в данном блоке будет проверяться во время его выполнения)
            SaveFile() # Вызываем функцию, сохраняющую файл
        except: # Если возникло исключение ("ошибка")
            dialog.focus_get() # Возвращаем фокус главному окну
            dialog.destroy() # Уничтожаем диалоговое окно
        else: # Если всё хорошо
            dialog.destroy() # Уничтожаем диалоговое окно
            root.destroy() # Уничтожаем главное окна
            
    #Создание элементов в диалоговом окне
    button_yes = Button(dialog, text='Да', width=9, command=SaveAndExit, cursor='hand2') # Кнопка "Да" с шириной 9, команда при нажатии - функция "Сохранить и выйти", курсор при наведении - "Рука"
    button_no = Button(dialog, text='Нет', width=9, command=root.destroy, cursor='hand2') # Кнопка "Нет" с шириной 9, команда при нажатии - уничтожение главного окна, курсор при наведении - "Рука"
    #Позиционирование элементов в диалоговом окне    
    Top_frame.pack(pady=10) # Верхний фрейм с отступами сверху и снизу 10
    Bot_frame.pack(side=BOTTOM, pady=5) # Нижний фрейм прижимаем вниз, отступ по вертикали 5
    label.pack() # Размещаем надпись
    button_yes.pack(side=LEFT, padx=10) # Кнопка, прижатая влево, отступ слева и справа 10
    button_no.pack(side=RIGHT, padx=10) # Кнопка, прижатая вправо, отступ слева и справа 10

    dialog.focus_set() # Установка фокуса на диалоговом окне
    dialog.grab_set() # Перехватываем все события с главного окна (пока открыто диалоговое окно, с главным окном взаимодействие отключено, кроме передвижения)
    dialog.wait_window() # Диалоговое окно ожидает уничтожения, а после передаёт управление главному 


def TextStyleBold(event): # Функция, срабатывающая при комбинации клавиш Control+b
    global count # Указываем, что переменная count является глобальной (взаимодействовать с ней можно из данной функции, хотя сама переменная объявлена в другой области видимости)
    
    if textEdit.tag_ranges('sel'): # Условие: Если тег будет 'sel' (по сути, это выделенный текст)
        textEdit.tag_add(f'styletag_{count}', SEL_FIRST,SEL_LAST) # Создаём тег для выделенного текста (Имя, первый индектс, второй индекст)
        textEdit.tag_configure(f'styletag_{count}', font=("Verdana", 12, "bold")) # Устанавливаем стиль для тега с именем styletag_{значение переменной count в данный момет}, шрифт=("название шрифта", размер шрифта, "полужирный")
        count += 1 # Увеличиваем переменную count на 1 (Этот счётчик хранит количество стилей, которые заданы текстку (полужирный и т.п.))

def TextStyleNormal(event): # Функция, срабатывающая при комбинации клавишь Control+n
    global count # Указываем, что переменная count является глобальной (взаимодействовать с ней можно из данной функции, хотя сама переменная объявлена в другой области видимости)
    
    if textEdit.tag_ranges('sel'): # Условие: Если тег будет 'sel' (по сути, это выделенный текст)
        textEdit.tag_add(f'styletag_{count}', SEL_FIRST,SEL_LAST) # Создаём тег для выделенного текста (Имя, первый индектс, второй индекст)
        textEdit.tag_configure(f'styletag_{count}', font=("Verdana", 12)) # Устанавливаем стиль для тега с именем styletag_{значение переменной count в данный момет}, шрифт=("название шрифта", размер шрифта, "полужирный")
        count += 1 # Аналогично предыдущей функции

def StyleEdit(): # Функция, создающая диалоговое окно редактора стилей
    dialog = Toplevel(root) # Создаём дочернее окно от root
    dialog.geometry('200x100+850+450') # Размер и смещение
    dialog.resizable(False, False) # Запрет на изменение размеров

    def cliked(): # Функция, срабатывающая при нажатии на кнопку "Ок"
        global count # Глобальная
        value = combo.get() # Получаем выбранное значение из выпадающего списка
        if value == 'Обычный': # Условие
            if textEdit.tag_ranges('sel'): # Выделенный текст
                textEdit.tag_add(f'styletag_{count}', SEL_FIRST,SEL_LAST) # Создаём тег
                textEdit.tag_configure(f'styletag_{count}', font=("Verdana", 12,)) # Применяем стиль к тегу
                count += 1 # Увеличиваем счётчик на 1
        elif value == 'Полужирный': # Условие
            if textEdit.tag_ranges('sel'): # Выделенный текст
                textEdit.tag_add(f'styletag_{count}', SEL_FIRST,SEL_LAST) # Создаём тег
                textEdit.tag_configure(f'styletag_{count}', font=("Verdana", 12, "bold")) # Применяем стиль
                count += 1 # Увеличиваем на 1
        elif value == 'Удалить все стили': # Условие
            for i in range(0, count): # Создаём цикл, который будет выполняться столько раз, сколько мы создали стилей
                textEdit.tag_delete(f'styletag_{i}') # Удалаяем стиль с тегом styletag_{значение i в данный момент}
                count -= 1 # Уменьшаем счётчик на 1
        dialog.destroy() # Уничтожаем диалоговое окно

    #Создание элементов в диалоговом окне
    label = Label(dialog, text='Выберите стиль текста') # Надпись
    combo = ttk.Combobox(dialog, value=["Обычный", "Полужирный", "Удалить все стили"], state="readonly", width=15) # Выпадающий список. state="readonly" - режим только чтения (изменять значение текстового поля изменять нельзя, можно только выбирать уже из предложенных)
    button = Button(dialog, text='Ок', command=cliked, width=10, cursor='hand2') # Кнопка "Ок". При нажатии вызовется функция clicked. Ширина 10, курсор при наведении - "рука"
    #Позиционирование элементов в диалоговом окне    
    label.pack(pady=4) # Размещаем надпись
    combo.pack(pady=5) # Выпадающий список
    button.pack(side=BOTTOM, pady=5) # Кнопку прижимаем книзу

    #Настройка элементов
    dialog.focus_set() # Установка фокуса на диалоговом окне
    dialog.grab_set() # Перехватываем все события с главного окна (пока открыто диалоговое окно, с главным окном взаимодействие отключено, кроме передвижения)
    dialog.wait_window() # Диалоговое окно ожидает уничтожения, а после передаёт управление главному 

# Создание элементов
#Меню
mainMenu = Menu(top_frame, font=("Verdana", 20, "bold"), tearoff=2) # Создаём меню, помещаем в верхний фрейм, (шрифт), "отрываем" от главного окна
root.config(menu=mainMenu) # Определяем mainMenu как меню окна

fileMenu = Menu(mainMenu, tearoff=0) # Создаём новый экземпляр меню, не отрывая
fileMenu.add_command(label="Открыть...", command=OpenFile) # Наналогично
fileMenu.add_command(label='Сохранить...', command=SaveFile)
fileMenu.add_command(label="Выход", command=ExitProgramm)

 
mainMenu.add_cascade(label="Файл", menu=fileMenu) # Создаём каскад меню, помешая в него fileMenu (При нажатии на пункт "файл" будт открываться каскадный список)
mainMenu.add_command(label='Редактор стилей', command=StyleEdit) # Команда

#Текстовое поле
textEdit = Text(bot_frame, font=("Verdana", 12), state=DISABLED) # Создаём текстовое поле в нижнем фрейме, задаём шрифт. Режим - редактирование отключено

#СкролБар
scroll = Scrollbar(textEdit, command=textEdit.yview, cursor='hand2') # Создаём скролбар в текстовом поле. Команда - Перемещение по оси y (вертикально) внутри поля. Курсор при наведении - рука

# Размещение элементов
#Фреймы
top_frame.pack(side=TOP) # Прижимаем фрейм вверх
bot_frame.pack(expand=True, fill = BOTH, pady=40, padx=40) # Размещаем следом нижний фрейм (expand=True - пока значение True, элемент (фрейм) заполняет всё доступное пространство внутри блока, 
#fill - растяжение элемента при изменеии размера окна = BOTH - Заполняет всё пространосто по вертикали и горизонатли внутри блока при растяжении)

#Элементы
textEdit.pack(expand=True, fill = BOTH) # Размещаем текстовое поле (параметры аналогичны, за исключением отступов)
scroll.pack(side=RIGHT, fill=Y) # Размещаем скролбар справа по оси Y (вертикально)

#Настройки элементов
textEdit.config(yscrollcommand=scroll.set) # Устанавливаем конфигурацию текстового поля: перемещение содержимого внутри поля по оси y

#Обработка событий
count = 0 # Счётчик для подсчёта изменненного текста (стилей)
textEdit.bind('<Control-b>', TextStyleBold) # Событие: При комбинации клавиш Control-b срабатывает функция TextStyleBold
textEdit.bind('<Control-n>', TextStyleNormal) # Событие: При комбинации клавиш Control-n срабатывает функция TextStyleNormal


root.mainloop() # Запускаем безконечный цикл окна. Он преврётся только в случае уничтожения окна