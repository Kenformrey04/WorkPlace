def Calculate(): # Функция
    """Блок из лабы 7"""
    # Импорт модулей
    import random 
    import module

    data = ''
    arr = []

    file = open('data/list7.1.txt', 'r')
    for i in file:
        data += i
    file.close()

    data = data.split(',')
    arr = []

    for i in data:
        arr.append(int(i))

    data = ''
    arr2 = []
    arr2 = module.function(arr, arr2)
    dic = dict(zip(arr, arr2))
    """END"""


    for key, value in dic.items(): # Цикл для перебора ключей и значений словаря
        data += f'{key}: {value}\n' # Присваиваем в переменную строку с {ключ}: {значение} перенос строки
    
    return [arr, data] # Возвращаем список из списка аргуменов и строку из {ключ}: {значение} перенос строки