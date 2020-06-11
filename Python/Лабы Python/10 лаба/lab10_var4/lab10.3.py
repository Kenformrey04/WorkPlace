# Импорт модуля
import numpy as np 

arr = np.array([ # Создаём массив numpy из двумерного списка
    [5,6,1,4,7,5,5,8],
    [-1,6,7,3,9,6,3,5],
    [-7,4,2,8,2,5,5,2],
    [-1,7,4,4,7,3,1,7],
    [7,9,2,7,4,1,7,5],
    [-4,8,2,1,6,8,5,4]
])
# Создаём условие: если остаток от деления на 2 не равен нулю, то число является нечётным
condition = arr %2 != 0 
# Поиск элементов, удовлетворяющих условию. Суммирование элементов
result = sum(np.extract(condition, arr)) 
print(result) # Вывод результата на экран



