def Calculate(valueA, valueB, valueC): # Функция находящее решение квадратного уравнения
    # Импорт модуля
    import math


    D = valueB * valueB - 4 * valueA * valueC # Вычисляем дискрименант
    if D < 0: # Условие
        return 'Нет решения!' # Возвращаем строку
    elif D == 0: # Условие иначе если
        return f'x = {-valueB / 2 * valueA}' # Возвращаем строку
    elif D > 0: # Условие иначе если
        return f'x1 = {-valueB + math.sqrt(D) / 2 * valueA}\nx2 = {-valueB - math.sqrt(D) / 2 * valueA}' # Возвращаем строку