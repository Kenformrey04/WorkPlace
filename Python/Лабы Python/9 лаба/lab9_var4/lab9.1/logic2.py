def Calculate(valueA, valueB, valueC):
    import math


    D = valueB * valueB - 4 * valueA * valueC
    if D < 0: # Условие
        return 'Нет решения!'
    elif D == 0: # Условие иначе если
        return f'x = {-valueB / 2 * valueA}'
    elif D > 0: # Условие иначе если
        return f'x1 = {-valueB + math.sqrt(D) / 2 * valueA}\nx2 = {-valueB - math.sqrt(D) / 2 * valueA}'