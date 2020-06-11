"""Коммантарии в lab9.1"""
def Calculate():
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

    del(data)
    data = ''
    arr2 = []
    arr2 = module.function(arr, arr2)
    dic = dict(zip(arr, arr2))


    for key, value in dic.items():
        data += f'{key}: {value}\n'
    
    return [arr, data]