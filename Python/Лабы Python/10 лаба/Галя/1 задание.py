import os

def Show_way(cur):
    for dr in os.listdir(cur):#os.listdir(cur) - список файлов и директорий в папке.
        abs_path = os.path.join(cur, dr)#Обьединяет путь который мы ввели - с каждым файлом по очереди в каталоге,и преобразует все в одну строку
        print(abs_path)

        if os.path.isdir(abs_path):#Проверяет существует ли указанный путь
            Show_way(abs_path)#рекурсия

def sum_digits(num):
# допустим ввели 58, сначала посчитаем 58 % 10 = 8 , потом прибавим  58 // 10 = 5, т.е 5 + 8  = 13
    return num % 10 + sum_digits(num//10) if num > 9 else num

exit = 0
while exit != 1:
    select = int(input('Какую операцию выполнить?\n\t1 - Рекурсивный обход папок,выводим содержимое каталога;\n\t2 - Сумма цифр числа;\
    \n\texit - выход из программы\n\nEnter:\t'))
    if select == 1:
        os.system('cls')
        Path = input('Введите путь каталога,содержимое которого хотите вывести:\t')
        print(Show_way(Path))

    elif select == 2:
        os.system('cls')
        value = int(input('Введите число:\t'))
        print(sum_digits(value))

    elif select == 'exit':
        os.system('cls')
        exit = 1
    else:
        print('Вы ввели неверную команду!')
        temp = input('Для продолжения нажмите клавишу "Enter"...')
        os.system('cls')


# F:\Каталог

