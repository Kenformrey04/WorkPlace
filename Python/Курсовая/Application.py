import tkinter as tk
import numpy as np
from time import sleep
from Ship import Ship
from random import randint
from random import choice


class Application(tk.Frame):
    # Глобальные атрибуты
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']  # Список букв
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Список цифр
    pointsAround = []
    userShipQuantity = 0
    compShipQuantity = 0
    compPointsShot = []
    tempHitPoints = []

    def __init__(self, root):
        super().__init__(root)
        self.init_app()

    def init_app(self):
        self.configure(bg='#AFEEEE')
        # Меню
        self.mainMenu = tk.Menu(self)
        self.fileMenu = tk.Menu(self, tearoff=0)
        self.fileMenu.add_command(
            label='Начать игру', command=self.RestartGame)
        self.mainMenu.add_cascade(label='Игра', menu=self.fileMenu)
        # Холст
        self.canvas = tk.Canvas(self, bg='white', width=950, height=600)
        self.canvas.pack(pady=30)
        # Старт игры
        self.StartGame()
        self.canvas.bind("<Button-1>", self.UserShot)
    def StartGame(self):  # Запуск игры
        self.CreatePlayersFields()  # Создание полей
        self.CreatePlayersFleet()  # Создание флотилии

    def CreatePlayersFields(self):  # Создание полей
        self.CreateUserField()
        self.CreateCompField()
    def CreatePlayersFleet(self):  # Создание флота
        self.CreateUserFleet()
        self.CreateCompFleet()

    def CreateUserField(self):
        self.canvas.create_polygon([40, 40], [440, 40], [440, 440], [
                                   40, 440], fill='white', outline='black', width=0)  # Создание поля
        for i in range(len(self.letters)):  # Создание букв
            location = 60
            self.canvas.create_text(
                [25, location + 40 * i], text=self.letters[i])
        for i in range(len(self.numbers)):  # Создание цифр
            location = 60
            self.canvas.create_text(
                [location + i * 40, 25], text=self.numbers[i])
        locationX = 40
        locationY = 40
        count = 0
        for row in range(0, 10):
            for col in range(0, 10):
                self.canvas.create_polygon(
                    [col * 40 + locationX, row * 40 + locationY], [col *
                                                                   40 + locationX + 40, row * 40 + locationY],
                    [col * 40 + locationX + 40, row * 40 + locationY + 40], [col * 40 + locationX, row * 40 + locationY + 40], fill='#00BFFF', outline='black', tags=f'UserBox_({row},{col})'
                )
                count += 1

    def CreateCompField(self):
        self.canvas.create_polygon([500, 40], [900, 40], [900, 440], [
                                   500, 440], fill='white', outline='black', width=0)  # Создание поля
        for i in range(len(self.letters)):  # Создание букв
            location = 60
            self.canvas.create_text(
                [485, location + 40 * i], text=self.letters[i])

        for i in range(len(self.numbers)):  # Создание цифр
            location = 520
            self.canvas.create_text(
                [location + i * 40, 25], text=self.numbers[i])
        locationX = 500
        locationY = 40
        count = 0
        for row in range(0, 10):
            for col in range(0, 10):
                self.canvas.create_polygon(
                    [col * 40 + locationX, row * 40 + locationY], [col *
                                                                   40 + locationX + 40, row * 40 + locationY],
                    [col * 40 + locationX + 40, row * 40 + locationY + 40], [col * 40 + locationX, row * 40 + locationY + 40], fill='#00BFFF', outline='black', tags=f'CompBox_({row},{col})'
                )
                count += 1

    def CreateUserFleet(self):  # Флот пользователя
        # Случайное число для выбора растановки кораблей
        select = randint(1, 5)
        # Создание экземпляра Ship
        self.userFirstShip = Ship(self.canvas, 'User', 1, select, self)
        self.userSecondShip = Ship(self.canvas, 'User', 2, select, self)
        self.userThirdShip = Ship(self.canvas, 'User', 3, select, self)
        self.userFourthShip = Ship(self.canvas, 'User', 4, select, self)
        self.userFifthShip = Ship(self.canvas, 'User', 5, select, self)
        self.userSixthShip = Ship(self.canvas, 'User', 6, select, self)
        self.userSeventhShip = Ship(self.canvas, 'User', 7, select, self)
        self.userEighthShip = Ship(self.canvas, 'User', 8, select, self)
        self.userNinthShip = Ship(self.canvas, 'User', 9, select, self)
        self.userTenthShip = Ship(self.canvas, 'User', 10, select, self)

        # Массив Кораблей
        self.UserShips = [self.userFirstShip, self.userSecondShip, self.userThirdShip, self.userFourthShip, self.userFifthShip,
                          self.userSixthShip, self.userSeventhShip, self.userEighthShip, self.userNinthShip, self.userTenthShip]
        self.userShipQuantity = 10  # Количество живых кораблей

    def CreateCompFleet(self):
        select = randint(1, 5)  # Выбор расстановки
        # Создание экземпляра корабля
        self.compFirstShip = Ship(self.canvas, 'Comp', 1, select, self)
        self.compSecondShip = Ship(self.canvas, 'Comp', 2, select, self)
        self.compThirdShip = Ship(self.canvas, 'Comp', 3, select, self)
        self.compFourthShip = Ship(self.canvas, 'Comp', 4, select, self)
        self.compFifthShip = Ship(self.canvas, 'Comp', 5, select, self)
        self.compSixthShip = Ship(self.canvas, 'Comp', 6, select, self)
        self.compSeventhShip = Ship(self.canvas, 'Comp', 7, select, self)
        self.compEighthShip = Ship(self.canvas, 'Comp', 8, select, self)
        self.compNinthShip = Ship(self.canvas, 'Comp', 9, select, self)
        self.compTenthShip = Ship(self.canvas, 'Comp', 10, select, self)

        self.CompShips = [self.compFirstShip, self.compSecondShip, self.compThirdShip, self.compFourthShip, self.compFifthShip,
                          self.compSixthShip, self.compSeventhShip, self.compEighthShip, self.compNinthShip, self.compTenthShip]
        self.compShipQuantity = 10  # Количество кораблей
        self.pointsAround = []  # Точки поблизости
        self.compPointsShot = []  # Точки выстрелов компьютера
        # Временные точки предыдущих попаданий (хранятся, пока корабль не убит)
        self.tempHitPoints = []
        self.check = 0  # Проверка (если попаданий 2 - check = 1, 2- check = 2)

    def UserShot(self, event):  # Метод выстрела пользователя
        self.OpenDialog()  # Проверка окончания игры
        # Определение координаты на холсте
        coordY = self.canvas.canvasy(event.y)
        coordX = self.canvas.canvasx(event.x)

        items = []  # Список для хранения найденных элементов

        # Нахождение элементов в радиусше 41 px
        # Поиск элемента на холсте по координатам
        item = self.canvas.find_overlapping(
            coordX, coordY, coordX, coordY - 41)
        for i in item:
            items.append(i)
        item = self.canvas.find_overlapping(
            coordX, coordY, coordX + 41, coordY)
        for i in item:
            items.append(i)
        item = self.canvas.find_overlapping(
            coordX, coordY, coordX, coordY + 41)
        for i in item:
            items.append(i)
        item = self.canvas.find_overlapping(
            coordX, coordY, coordX - 41, coordY)
        for i in item:
            items.append(i)
        max = 4  # Максимальное число вхождений
        for i in items:  # Проход по элементам
            if items.count(i) >= max:  # Если число вхождений i больше либо равно максимального
                max = items.count(i)  # Обновление максиумума
                item = i  # Перезапись элемента
        try:
            tag = self.canvas.gettags(item)[0]  # Получение нужного тега
            if tag[0:4:1] == 'Comp':
                item = self.canvas.find_withtag(tag)
                self.canvas.itemconfig(item, fill='white')
        except:
            pass
        else:
            if tag[0:4:1] == 'Comp':  # Если срез тега == Comp
                self.compPointY = int(tag[-4])  # Точка по Y
                self.compPointX = int(tag[-2])  # Точка по X
            elif tag[0:4:1] != 'Comp':
                return 0
            self.shotResult = 0  # Зануление результата выстрела
            for ship in self.CompShips:  # Проверка совпадения координат выстрела по кораблю
                # Вызов метода выстрела у каждого корабля противника
                shot = ship.Shot(self.compPointY, self.compPointX,
                                 self.shotResult, self.compShipQuantity)
                if shot > 0:  # Если выстрел является попаданием
                    self.shotResult = shot  # Обновление результата выстрела
                    break  # Прекращение проверки
            if self.shotResult == 1 or self.shotResult == 2:
                if self.shotResult == 1:
                    # Окрашивание клетки в красный
                    self.canvas.itemconfig(item, fill='red')
                    return 0  # Выход из функции
                elif self.shotResult == 2:
                    self.canvas.itemconfig(item, fill='#FF6347')
                    items = self.canvas.find_withtag(
                        'kill')  # Поиск элемента с тегом kill
                    for item in items:  # закрпшивание элементов в чёрный
                        self.canvas.itemconfig(item, fill='#FF6347', tags='dead')
                    self.compShipQuantity -= 1  # Уменьшение количества кораблей на 1
                    self.OpenDialog()  # Проверка победителя
                return 0  # Прерывание фунции
            elif self.shotResult == 0:
                self.canvas.itemconfig(
                    item, fill='white', tags='miss')  # Окраска в белый
                self.CompShot()  # Вызов выстрела компьютера

    def CompShot(self):  # Выстрел копьютера
        if len(self.tempHitPoints) != 0:  # Если попадания имеются
            if len(self.pointsAround) != 0:  # Если точки поблизости имеются
                if self.check == 0:
                    try:
                        self.ChoiceRandomPointsAround()  # Рандомный выбор из точек поблизости
                    except:
                        pass  # Очередной костыль
                elif self.check == 1:
                    self.userPointY = self.pointsAround[-1][0]
                    self.userPointX = self.pointsAround[-1][1]
                    # Удаление из точек поблизости
                    self.pointsAround.remove(self.pointsAround[-1])
                    self.check = 2
                elif self.check == 2:
                    self.userPointY = self.pointsAround[0][0]
                    self.userPointX = self.pointsAround[0][1]
                    self.pointsAround.remove(self.pointsAround[0])
                elif self.check == 3:
                    self.userPointY = self.pointsAround[0][0]
                    self.userPointX = self.pointsAround[0][1]
                    self.pointsAround = []
                    self.check = 0
            else:
                if len(self.tempHitPoints) == 1:  # Если текущее попадание 1
                    self.GenerationPointsAround()  # Генерация точек поблизости
                    try:  # Костыль)
                        self.ChoiceRandomPointsAround()  # Разномный выбор из точек поблизости
                    except:
                        self.GenerationPointsAround()  # Генерация точек поблизости
                        try:
                            self.ChoicePointsAround()  # Явный выбор из точек поблизости
                        except:
                            pass  # Тоже костыль)))
                elif len(self.tempHitPoints) == 2:  # Если попаданий 2
                    # Получение точек поблизости в плоскости данного корабля (при 2-х попаданиях можно определить плоскость: либо горизонталь, либо вертикаль)
                    self.IdentifyPointsAround()
                    self.userPointY = self.pointsAround[-1][0]
                    self.userPointX = self.pointsAround[-1][1]
                    self.pointsAround.remove(self.pointsAround[-1])
                    self.check = 1
                elif len(self.tempHitPoints) == 3:  # Если попаданий 3
                    # Генерация точек поблизости, ихсодя из предыдущих ПОПАДАНИЙ
                    self.ChoiceInLastCompShotPointsByIdentifyPointsAround()
                    try:  # Костыль
                        self.userPointY = self.pointsAround[-1][0]
                        self.userPointX = self.pointsAround[-1][1]
                        self.pointsAround.remove(self.pointsAround[-1])
                    except:
                        self.IdentifyPointsAround()
                        self.userPointY = self.pointsAround[-1][0]
                        self.userPointX = self.pointsAround[-1][1]
                        self.pointsAround.remove(self.pointsAround[-1])
        else:
            # Если нет точек поблизости и текущих пападаний нет (нет раненого корабля), то генерируется случайная точка
            self.GenerationRandomPoints()
        self.CheckCompShot()  # ВЫзов метода, определяющего результат попадания
        # Проверка: было ли попадание
        if self.shotResult == 0:  # Попадания не было
            item = self.canvas.find_withtag(
                f'UserBox_({self.userPointY},{self.userPointX})')
            self.canvas.itemconfig(item, fill='white', tags='miss')
        elif self.shotResult == 1:  # Корабль ранен
            if len(self.tempHitPoints) == 2:  # Если попаданий в текущий корабль было 2
                self.check = 1
            elif len(self.tempHitPoints) == 3:  # Если было 3
                self.check = 3
            self.CompShot()  # Рекурсивный вызов функции выстрела компьютера (Всё начинается заново)
        elif self.shotResult == 2:  # Если корабль убит
            self.userShipQuantity -= 1  # Уменьшение кораблей на 1
            self.OpenDialog()  # Проверка победителя
            self.shotResult = 0  # Обнуление результата выстрела
            self.tempHitPoints = []  # Обнуление текущих попаданий
            self.pointsAround = []  # Обнуление точек поблизости
            self.check = 0  # Обнуление
            self.CompShot()  # Рекурсивный вызов метода

    def OpenDialog(self):  # Функция, определяющая победителя
        def CloseDialog():  # Закрытие диалогового окна
            self.RestartGame()  # Рестарт игры
            dialog.destroy()
        if self.userShipQuantity == 0 or self.compShipQuantity == 0:  # Определение победителя
            if self.userShipQuantity == 0:
                winer = 'Компьютер'
            elif self.compShipQuantity == 0:
                winer = 'Пользователь'
            dialog = tk.Toplevel(self)  # Создание дочернего окна
            dialog.geometry("200x80+500+200")
            dialog.resizable(False, False)
            dialog.focus_set()  # Передача фокуса
            dialog.grab_set()  # Перехват событий с главного окна
            label = tk.Label(dialog, text=f'Победитель {winer}!')
            button = tk.Button(dialog, text='ОК',
                               command=CloseDialog, width=12)
            label.place(y=10, x=25)
            button.place(y=45, x=55)

    # Выбор рандомной пары точек из точек поблизости
    def ChoiceRandomPointsAround(self):
        while 1:
            if len(self.pointsAround) == 4:
                select = randint(0, 3)
            elif len(self.pointsAround) == 3:
                select = randint(0, 2)
            elif len(self.pointsAround) == 2:
                select = randint(0, 1)
            else:
                select = 0
            self.userPointY = self.pointsAround[select][0]
            self.userPointX = self.pointsAround[select][1]
            if [self.userPointY, self.userPointX] not in self.compPointsShot:
                self.pointsAround.remove([self.userPointY, self.userPointX])
                break
            else:
                if len(self.pointsAround) == 0:
                    break
                self.pointsAround.remove([self.userPointY, self.userPointX])

    def ChoicePointsAround(self):  # Явный выбор из точек поблизости
        count = 0
        while 1:
            if len(self.pointsAround) > 0:
                self.userPointY = self.pointsAround[count][0]
                self.userPointX = self.pointsAround[count][1]
                if [self.userPointY, self.userPointX] not in self.compPointsShot:
                    self.pointsAround.remove(
                        [self.userPointY, self.userPointX])
                    break
                else:
                    if len(self.pointsAround) == 0:
                        break
                    self.pointsAround.remove(
                        [self.userPointY, self.userPointX])
            else:
                self.ChoiceInLastCompShotPointsByIdentifyPointsAround()
                break
            count += 1
            if count == 3:
                break
    # Добавление пустых клеток вокруг убитого корабля в выстрелы компьютера (чтобы не было выстрелов в них)
    def AddClearCoordInCompPointsShot(self, ship):
        clearPointsY = ship.clearCoord[0]
        clearPointsX = ship.clearCoord[1]
        for i in range(len(clearPointsY)):
            self.compPointsShot.append([clearPointsY[i], clearPointsX[i]])
    def IdentifyPointsAround(self):  # Определение точек поблизости в 1 плоскости
        tempY = []
        tempX = []
        for item in self.tempHitPoints:
            tempY.append(item[0])
            tempX.append(item[1])
        trendY = tempY[-1] - tempY[0]
        trendX = tempX[-1] - tempX[0]
        if trendY == 0:
            if trendX > 0:
                self.pointsAround = [[tempY[0], tempX[0] + 3], [tempY[0], tempX[0] + 2], [
                    tempY[0], tempX[0] + 1], [tempY[0], tempX[0] + 2]]
            elif trendX < 0:
                self.pointsAround = [[tempY[0], tempX[0] - 3], [tempY[0], tempX[0] - 2], [
                    tempY[0], tempX[0] - 1], [tempY[0], tempX[0] - 2]]
        elif trendX == 0:
            if trendY > 0:
                self.pointsAround = [[tempY[0] + 3, tempX[0]], [tempY[0] + 2,
                                                                tempX[0]], [tempY[0] + 1, tempX[0]], [tempY[0] + 2, tempX[0]]]
            elif trendY < 0:
                self.pointsAround = [[tempY[0] - 3, tempX[0]], [tempY[0] - 2,
                                                                tempX[0]], [tempY[0] - 1, tempX[0]], [tempY[0] - 2, tempX[0]]]
        if len(self.pointsAround) == 4:
            n = 4
        elif len(self.pointsAround) == 3:
            n = 3
        elif len(self.pointsAround) == 2:
            n = 2
        elif len(self.pointsAround) == 1:
            n = 1
        else:
            pass
        count = 0
        while 1:
            if self.pointsAround[count][0] < 0 or self.pointsAround[count][0] > 9 or self.pointsAround[count][1] < 0 or self.pointsAround[count][1] > 9 or self.pointsAround[count] in self.compPointsShot:
                self.pointsAround.remove(self.pointsAround[count])
                n -= 1
            count += 1
            if count >= n:
                break
    def GenerationRandomPoints(self):  # Генерация рандомной точки
        while 1:  # Генерация точек для выстрела
            pointY = randint(0, 9)  # Генерация случайной точки. по y
            pointX = randint(0, 9)
            # Если точки не совпадают с точками предыдущих выстрелов
            if [pointY, pointX] not in self.compPointsShot:
                self.userPointY = pointY
                self.userPointX = pointX
                break

    def CheckCompShot(self):  # Проверка выстрела
        self.shotResult = 0
        self.compPointsShot.append([self.userPointY, self.userPointX])
        for ship in self.UserShips:  # Выстрел
            shot = ship.Shot(self.userPointY, self.userPointX,
                             self.shotResult, self.userShipQuantity)
            if shot > 0:
                self.shotResult = shot
                if self.shotResult == 2:
                    self.AddClearCoordInCompPointsShot(ship)
                if [self.userPointY, self.userPointX] not in self.tempHitPoints:
                    if self.shotResult == 1:
                        self.tempHitPoints.append(
                            [self.userPointY, self.userPointX])
                break
    def GenerationPointsAround(self):  # Определение точек поблизости
        if self.userPointY == 0 and self.userPointX == 0:
            self.pointsAround = [
                [self.userPointY + 1, self.userPointX], [self.userPointY, self.userPointX + 1]]
        elif self.userPointY == 0 and self.userPointX == 9:
            self.pointsAround = [
                [self.userPointY + 1, self.userPointX], [self.userPointY, self.userPointX - 1]]
        elif self.userPointY == 9 and self.userPointX == 0:
            self.pointsAround = [
                [self.userPointY - 1, self.userPointX], [self.userPointY, self.userPointX + 1]]
        elif self.userPointY == 9 and self.userPointX == 9:
            self.pointsAround = [
                [self.userPointY - 1, self.userPointX], [self.userPointY, self.userPointX - 1]]
        elif self.userPointY == 0 and self.userPointX > 0 and self.userPointX < 9:
            self.pointsAround = [[self.userPointY, self.userPointX - 1], [
                self.userPointY + 1, self.userPointX], [self.userPointY, self.userPointX + 1]]
        elif self.userPointY == 9 and self.userPointX > 0 and self.userPointX < 9:
            self.pointsAround = [[self.userPointY, self.userPointX - 1], [
                self.userPointY - 1, self.userPointX], [self.userPointY, self.userPointX + 1]]
        elif self.userPointX == 0 and self.userPointY > 0 and self.userPointY < 9:
            self.pointsAround = [[self.userPointY - 1, self.userPointX], [
                self.userPointY, self.userPointX + 1], [self.userPointY + 1, self.userPointX]]
        elif self.userPointX == 9 and self.userPointY > 0 and self.userPointY < 9:
            self.pointsAround = [[self.userPointY - 1, self.userPointX], [
                self.userPointY, self.userPointX - 1], [self.userPointY + 1, self.userPointX]]
        elif self.userPointY > 0 and self.userPointY < 9 and self.userPointX > 0 and self.userPointX < 9:
            self.pointsAround = [[self.userPointY - 1, self.userPointX], [self.userPointY, self.userPointX + 1], [
                self.userPointY + 1, self.userPointX], [self.userPointY, self.userPointX - 1]]

    # определение точек поблизости в 1 плоскости (если аналогичный метод не подействовал)
    def ChoiceInLastCompShotPointsByIdentifyPointsAround(self):
        # Временные точки, необходимые для определения точек поблизости
        tempPointsY = [self.compPointsShot[-3][0], self.compPointsShot[-1][0]]
        tempPointsX = [self.compPointsShot[-3][1], self.compPointsShot[-1][1]]
        trendY = tempPointsY[1] - tempPointsY[0]
        trendX = tempPointsX[1] - tempPointsX[0]
        if trendY == 0:
            if trendX > 0:
                self.pointsAround = [[tempPointsY[1], tempPointsX[1] + 1], [tempPointsY[1], tempPointsX[1] + 2], [
                    tempPointsY[1], tempPointsX[1] - 1], [tempPointsY[1], tempPointsX[1] - 2]]
            elif trendX < 0:
                self.pointsAround = [[tempPointsY[1], tempPointsX[1] - 1], [tempPointsY[1], tempPointsX[1] - 2], [
                    tempPointsY[1], tempPointsX[1] + 1], [tempPointsY[1], tempPointsX[1] + 1]]
        elif trendX == 0:
            if trendY > 0:
                self.pointsAround = [[tempPointsY[1] + 1, tempPointsX[1]], [tempPointsY[1] + 2, tempPointsX[1]], [
                    tempPointsY[1] - 1, tempPointsX[1]], [tempPointsY[1] - 2, tempPointsX[1]]]
            elif trendY < 0:
                self.pointsAround = [[tempPointsY[1] - 1, tempPointsX[1]], [tempPointsY[1] - 2, tempPointsX[1]], [
                    tempPointsY[1] + 1, tempPointsX[1]], [tempPointsY[1] + 1, tempPointsX[1]]]
        if len(self.pointsAround) == 4:
            n = 4
        elif len(self.pointsAround) == 3:
            n = 3
        elif len(self.pointsAround) == 2:
            n = 2
        elif len(self.pointsAround) == 1:
            n = 1
        else:
            pass
        try:
            count = 0
            while 1:
                if self.pointsAround[count][0] < 0 or self.pointsAround[count][0] > 9 or self.pointsAround[count][1] < 0 or self.pointsAround[count][1] > 9 or self.pointsAround[count] in self.compPointsShot:
                    self.pointsAround.remove(self.pointsAround[count])
                    n -= 1
                count += 1
                if count >= n:
                    break
        except:
            pass
    def RestartGame(self):  # Рестарт игры
        for ship in self.UserShips:
            ship.__dell__()  # Вызов дестректора метода каждого корабля
        for ship in self.CompShips:
            ship.__dell__()
        items = self.canvas.find_all()  # Поиск всех элементов на холсте
        for item in items:
            self.canvas.delete(item)  # Удаление элементов с холста
        self.StartGame()  # Запуск игры
