"""Код из лабы 6"""
import math

def function(arr, arr2):
    for i in arr:
        if 0 < i < 10:
            x = 2 * math.exp(math.pi * i)
            arr2.append(x)

        elif i <= 0 and i >= 10:
            x = 0
            arr2.append(x)

    return arr2
"""END"""