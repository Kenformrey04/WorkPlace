import tkinter as tk
from random import randint
from random import choice

class Ship():
    # player = 'player' # Имя пользователя (User, Comp)
    # hp = 'health' # Текущее состояние корабля (от 4 до 0, где 0 - убит)
    # colorCell = 'color' # Цвет ячейки (Если ячейка User, то зелёная, если ячейка Comp, то ячейка голубая)

    one = { # Координаты кораблей (5 вариантов)
        1: [[0,1,2,3], [0]],
        2: [[9], [6,7,8,9]],
        3: [[4,5,6,7], [0]],
        4: [[1,2,3,4], [8]],
        5: [[0,1,2,3], [4]]
    }

    clearCoordOne = { # Пустые клетки вокруг корабля
        1: [[0,1,2,3,4,4], [1,1,1,1,1,0]],
        2: [[8,9,8,8,8,8], [5,5,6,7,8,9]],
        3: [[3,3,4,5,6,7,8,8], [0,1,1,1,1,1,1,0]],
        4: [[0,0,0,1,2,3,4,5,5,5,4,3,2,1], [7,8,9,9,9,9,9,9,8,7,7,7,7,7]],
        5: [[0,0,1,2,3,4,4,4,3,2,1], [3,5,5,5,5,5,4,3,3,3,3]]
    }

    two = {
        1: [[6,7,8], [1]],
        2: [[6], [2,3,4]],
        3: [[7], [2,3,4]],
        4: [[1,2,3], [1]],
        5: [[7,8,9], [6]]
    }

    clearCoordTwo = {
        1: [[5,5,5,6,7,8,9,9,9,8,7,6], [0,1,2,2,2,2,2,1,0,0,0,0]],
        2: [[5,5,5,5,5,6,7,7,7,7,7,6], [1,2,3,4,5,5,5,4,3,2,1,1]],
        3: [[6,6,6,6,6,7,8,8,8,8,8,7], [1,2,3,4,5,5,5,4,3,2,1,1]],
        4: [[0,0,0,1,2,3,4,4,4,3,2,1], [0,1,2,2,2,2,2,1,0,0,0,0]],
        5: [[6,6,6,7,8,9,9,8,7], [5,6,7,7,7,7,5,5,5]]
    }

    three = {
        1: [[5], [4,5,6]],
        2: [[0,1,2], [6]],
        3: [[0,1,2], [7]],
        4: [[9], [2,3,4]],
        5: [[5], [7,8,9]]
    }

    clearCoordThree = {
        1: [[4,4,4,4,4,5,6,6,6,6,6,5], [3,4,5,6,7,7,7,6,5,4,3,3]],
        2: [[0,0,1,2,3,3,3,2,1], [5,7,7,7,7,6,5,5,5]],
        3: [[0,0,1,2,3,3,3,2,1], [6,8,8,8,8,7,6,6,6]],
        4: [[8,8,8,8,8,9,9], [1,2,3,4,5,5,1]],
        5: [[4,4,4,4,6,6,6,6,5], [6,7,8,9,9,8,7,6,6]]
    }

    four = {
        1: [[1,2], [5]],
        2: [[9], [2,3]],
        3: [[1,2], [2]],
        4: [[0,1], [3]],
        5: [[0], [0,1]]
    }

    clearCoordFour = {
        1: [[0,0,0,1,2,3,3,3,2,1], [4,5,6,6,6,6,5,4,4,4]],
        2: [[8,8,8,8,9,9], [1,2,3,4,4,1]],
        3: [[0,0,0,1,2,3,3,3,2,1], [1,2,3,3,3,3,2,1,1,1]],
        4: [[0,0,1,2,2,2,1], [2,4,4,4,3,2,2]],
        5: [[0,1,1,1], [2,2,1,0]]
    }

    five = {
        1: [[0], [8,9]],
        2: [[0], [1,2]],
        3: [[9], [4,5]],
        4: [[4], [4,5]],
        5: [[6,7], [0]]
    }

    clearCoordFive = {
        1: [[0,1,1,1], [7,9,8,7]],
        2: [[0,0,1,1,1,1], [0,3,3,2,1,0]],
        3: [[8,8,8,8,9,9], [3,4,5,6,6,3]],
        4: [[3,3,3,3,4,5,5,5,5,4], [3,4,5,6,6,6,5,4,3,3]],
        5: [[5,5,6,7,8,8], [0,1,1,1,1,0]]
    }

    six = {
        1: [[3], [2,3]],
        2: [[1,2], [9]],
        3: [[7,8], [9]],
        4: [[6,7], [5]],
        5: [[2,3], [6]]
    }    

    clearCoordSix = {
        1: [[2,2,2,2,3,4,4,4,4,3], [1,2,3,4,4,4,3,2,1,1]],
        2: [[0,0,3,3,2,1], [8,9,9,8,8,8]],
        3: [[6,6,9,9,8,7], [8,9,9,8,8,8]],
        4: [[5,5,5,6,7,8,8,8,7,6], [4,5,6,6,6,6,5,4,4,4]],
        5: [[1,1,1,2,3,4,4,4,3,2], [5,6,7,7,7,7,6,5,5,5]]
    }

    seven = {
        1: [[8], [5]],
        2: [[4], [1]],
        3: [[9], [1]],
        4: [[8], [0]],
        5: [[4], [2]]
    }

    clearCoordSeven = {
        1: [[7,7,7,8,9,9,9,8], [4,5,6,6,6,5,4,4]],
        2: [[3,3,3,4,5,5,5,4], [0,1,2,2,2,1,0,0]],
        3: [[8,8,8,9,9], [0,1,2,2,0]],
        4: [[7,7,8,9,9], [0,1,1,1,0]],
        5: [[3,3,3,4,5,5,5,4], [1,2,3,3,3,2,1,1]]
    }

    eight = {
        1: [[3], [7]],
        2: [[9], [0]],
        3: [[5], [2]],
        4: [[5], [1]],
        5: [[8], [3]]
    }

    clearCoordEight = {
        1: [[2,2,2,3,4,4,4,3], [6,7,8,8,8,7,6,6]],
        2: [[8,8,9], [0,1,1]],
        3: [[4,4,4,5,6,6,6,5], [1,2,3,3,3,2,1,1]],
        4: [[4,4,4,5,6,6,6,5], [0,1,2,2,2,1,0,0]],
        5: [[7,7,7,8,9,9,9,8], [2,3,4,4,4,3,2,2]]
    }

    nine = {
        1: [[8], [8]],
        2: [[4], [3]],
        3: [[8], [7]],
        4: [[6], [7]],
        5: [[1], [8]]
    }

    clearCoordNine = {
        1: [[7,7,7,8,9,9,9,8], [7,8,9,9,9,8,7,7]],
        2: [[3,3,3,4,5,5,5,4], [2,3,4,4,4,3,2,2]],
        3: [[7,7,7,8,9,9,9,8], [6,7,8,8,8,7,6,6]],
        4: [[5,5,5,6,7,7,7,6], [6,7,8,8,8,7,6,6]],
        5: [[0,0,0,1,2,2,2,1], [7,8,9,9,9,8,7,7]],
    }

    ten = {
        1: [[3], [9]],
        2: [[6], [9]],
        3: [[5], [9]],
        4: [[8], [8]],
        5: [[9], [9]]
    }

    clearCoordTen = {
        1: [[2,2,4,4,3], [8,9,9,8,8]],
        2: [[5,5,7,7,6], [8,9,9,8,8]],
        3: [[4,4,6,6,5], [8,9,9,8,8]],
        4: [[7,7,7,8,9,9,9,8], [7,8,9,9,9,8,7,7]],
        5: [[8,8,9], [8,9,8]]
    }


    def __init__(self, canvas, player, ship, select, window): # Конструктор класса 
        self.player = player
        self.canvas = canvas
        self.select = select
        self.ship = ship
        self.window = window
        if self.player == 'User':
            self.color = '#00FF00'
        if self.player == 'Comp':
            self.color = '#00BFFF'
        self.CreateShip()


    def CreateShip(self):
        if self.ship == 1: # Определение корабля
            self.coordShip = self.one[self.select] # Получение координат корабля
            self.clearCoord = self.clearCoordOne[self.select] # Получение координат пустых клеток вокруг корабля
            self.hp = 4 # Здоровье корабля
        if self.ship == 2:
            self.coordShip = self.two[self.select]
            self.clearCoord = self.clearCoordTwo[self.select]
            self.hp = 3
        if self.ship == 3:
            self.coordShip = self.three[self.select]
            self.clearCoord = self.clearCoordThree[self.select]
            self.hp = 3
        if self.ship == 4:
            self.coordShip = self.four[self.select]
            self.clearCoord = self.clearCoordFour[self.select]
            self.hp = 2
        if self.ship == 5:
            self.coordShip = self.five[self.select]
            self.clearCoord = self.clearCoordFive[self.select]
            self.hp = 2
        if self.ship == 6:
            self.coordShip = self.six[self.select]
            self.clearCoord = self.clearCoordSix[self.select]
            self.hp = 2
        if self.ship == 7:
            self.coordShip = self.seven[self.select]
            self.clearCoord = self.clearCoordSeven[self.select]
            self.hp = 1
        if self.ship == 8:
            self.coordShip = self.eight[self.select]
            self.clearCoord = self.clearCoordEight[self.select]
            self.hp = 1
        if self.ship == 9:
            self.coordShip = self.nine[self.select]
            self.clearCoord = self.clearCoordNine[self.select]
            self.hp = 1
        if self.ship == 10:
            self.coordShip = self.ten[self.select]
            self.clearCoord = self.clearCoordTen[self.select]
            self.hp = 1
        
        self.pointsY = self.coordShip[0] # Точки по y
        self.pointsX = self.coordShip[1] # Точки по x

        for row in self.pointsY: # Закрашивание ячеек
            for col in self.pointsX:
                item = self.canvas.find_withtag(f'{self.player}Box_({row},{col})') # Поиск нужной ячейки
                self.canvas.itemconfig(item, fill=self.color) # Изменение цвета ячейки
        
    def Shot(self, pointY, pointX, result, shipQuantity, check=0): # Метод выстрела корабля (выстрел в текущий корабль)
        result = 0 # Промах
        if pointY in self.pointsY and pointX in self.pointsX:
            self.hp -= 1 
            item = self.canvas.find_withtag(f'{self.player}Box_({pointY},{pointX})')
            self.canvas.itemconfig(item, fill='red')
            if self.player == 'Comp':
                self.canvas.itemconfig(item, fill='red', tags='kill')
            result = 1 # Попадание
            if self.hp == 0:
                for row in self.pointsY: # Закрашивание убитых клеток корабля на чёрные
                    for col in self.pointsX:
                        item = self.canvas.find_withtag(f'{self.player}Box_({row},{col})')
                        self.canvas.itemconfig(item, fill='#FF6347', tags='dead')
                result = 2 # Гибель корабля
        if result == 2: # Если корабль убит
            shipQuantity -= 1 # Уменьшение количества кораблей
            clearPointsY = self.clearCoord[0]
            clearPointsX = self.clearCoord[1]
            for i in range(len(clearPointsY)): # Закрашивание пустых клеток вокруг корабля
                item = self.canvas.find_withtag(f'{self.player}Box_({clearPointsY[i]},{clearPointsX[i]})')
                self.canvas.itemconfig(item, fill='white', tags='None')
            
        return result

    
    

    
    def __dell__(self):
        del(self)