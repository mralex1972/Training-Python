# 1.	По двум заданным числам проверить является ли одно квадратом второго.
#
# a = int(input('Введите число '))
# b = int(input('Введите еще число '))
# if a**2 == b:
#     print(f'{a}^2 = {b}')
# elif b**2 == a:
#     print(f'{b}^2 = {a}')
# else:
#     print('Ни одно число не является квадратом другого')
#
# 2.	Найти максимальное из пяти чисел.
#
# list = [5,6,9,8,7]
# # for i in range(5):
#      print('Введите число')
#      list[i] = int(input())
# max = list[0]
# for j in range(1,5):
#     if list[j] > max:
#         max = list[j]
# print(f'Максимальное значение {max}')
#
# 3.	Вывести на экран числа от -N до N.
#
# n = int(input('Введите N  '))
# for i in range(-n,n+1):
#     print(i)
#
# 4.	Показать первую цифру дробной части числа.
#
# num = 456.821
# print(int(num*10)%int(num))
#
# 5.	Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30.
#
# print('Введите число')
# N = int(input())
# if N%5 == 0 and N%10 == 0 or N%15 == 0 and not(N%30 == 0):
#     print('Это правильное число')
# else:
#     print('Это неправильное число')
#
# 6.	Дано число обозначающее день недели.
#       Вывести его название и указать является ли он выходным.
#
# print('Введите номер дня недели')
# day = int(input())
# week = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
# if 1<=day<=5:
#     print(week[day-1])
# elif day == 6 or day == 7:
#     print(week[day-1])
#     print('Выходной')
# else:
#     print('Приходите завтра')
#
# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
#   для всех значений предикат.
#
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not(x or y or z) == (not(x) and not(y) and not(z)):
#                 print(f'При X = {x}  Y = {y}  Z = {z}  Истинно')
#             else:
#                 print(f'При X = {x}  Y = {y}  Z = {z}  Ложь') 
#
# 8. Сообщить в какой четверти координатной плоскости или на
#  какой оси находится точка с координатами Х и У. 
#
# x = int(input('Введите координату Х =  '))
# y = int(input('Введите координату Y =  '))
# if y == 0:
#     print('Точка лежит на оси абсцисс.')
# elif y > 0:
#     if x == 0:
#         print('Точка лежит на оси ординат.')
#     elif x > 0:
#         print('I четверть')
#     else:
#         print('II четверть')
# else:
#     if x == 0:
#         print('Точка лежит на оси ординат.')
#     elif x > 0:
#         print('IV четверть')
#     else:
#         print('III четверть')
#
# 9. Указав номер четверти прямоугольной системы координат,
#  показать допустимые значения координат для точек этой четверти.
#
# coord = ['X>0 ; Y>0', 'X<0 ; Y>0', 'X<0 ; Y<0', 'X>0 ; Y<0']
# quarter = int(input('Введите номер четверти  '))
# if 0<quarter<5:
#     print(coord[quarter - 1])
# else:
#     print('Шутник!')
#
# 10.	Найти расстояние между двумя точками пространства.
#
# print('Введите координаты точек (X1;Y1;Z1) и (X2;Y2;Z2)')
# x1 = float(input('X1 = '))
# y1 = float(input('Y1 = '))
# z1 = float(input('Z1 = '))
# x2 = float(input('X2 = '))
# y2 = float(input('Y2 = '))
# z2 = float(input('Z2 = '))
# dx = x2 - x1
# dy = y2 - y1
# dz = z2 - z1
# print(f'Расстояние между точками равно {round((dx**2 + dy**2 + dz**2)**0.5, 2)}')
#
# 11. Сформировать список из  N членов последовательности.
#     Для N = 5: 1, -3, 9, -27, 81 и т.д.
#
# n = int(input('Введите количество элементов последовательности '))
# list = [1]
# for i in range(n-1):
#     list.append(list[i] * (-3))
# print(list)
#
# 12.	Для натурального n создать словарь индекс-значение, состоящий
#  из элементов последовательности 3n + 1.
#  Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
#
# dictionary = {}
# n = int(input('Введите N  '))
# for i in range(1,n + 1):
#     dictionary[i] = 3 * i + 1
# print(dictionary)
#
# 13.	Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
#
# text = input('Введите исследуемый текст \n')
# search_text = input('Введите искомый текст \n')
# count = 0
# for i in range(len(text)-len(search_text)):
#     if text[i:i+len(search_text)] == search_text:
#         count += 1
# print(f'Искомый текст найден {count} раз.')
#
# 14.	Подсчитать сумму цифр в вещественном числе.
#
# import random
# N = str(random.random()*100)
# sum  = 0
# for i in range(len(N)):
#     if N[i].isdigit():
#         sum += int(N[i])
# print(f'Сумма цифр числа {N} равна {sum}')
#
# 15.	Написать программу получающую набор произведений чисел от 1 до N.
#  Пример: пусть N = 4, тогда[ 1, 2, 6, 24 ]
#
# n = int(input('Введите N = '))
# lst = []
# lst.append(1)
# for i in range(1,n):
#     lst.append(lst[i-1] * (i+1))
# print(lst)
#
# 16.	Задать список из n чисел последовательности (1+〖1/n)〗^n и вывести на экран их сумму.
#
# list = []
# n = int(input('Введите N '))
# for i in range(1,n+1):
#     list.append((1+ 1/i)**i)
# print(list)
# print(sum(list))
#
# 17.	Задать список из N элементов, заполненных числами из [-N, N].
#    Найти произведение элементов на указанных позициях.
#    Позиции хранятся в файле file.txt в одной строке одно число.
#
# n = int(input('Введите N '))
# list = []
# for i in range(2*n + 1):
#     list.append(i - n)
# print(list)
# data = open('file.txt', 'a')
# import random
# # Записываем в файл случайное количество случайных значений индексов
# # элементов списка:
# for i in range(2, random.randint(3, 2*n + 1)):
#     num = random.randint(0, 2*n)
#     data.writelines(f'{num}\n')
# data.close()
# data = open('file.txt', 'r')
# p = 1
# for line in data:
#     index = int(line)
#     p *= list[index]
# print(f'Произведение элементов равно {p}')
# data.close()

# 18.	Реализовать алгоритм перемешивания списка.
#
# list = [1,2,3,4,5,6,7,8,9,0]
# import random
# for i in range(len(list)):
#     media = list[i]
#     k = random.randint(1,len(list)-1)
#     list[i] = list[k]
#     list[k] = media
# print(list)
#
# 19.	Реализовать алгоритм задания случайных чисел.
#   Без использования встроенного генератора псевдослучайных чисел.
#
# min = int(input('Введите минимальное значение '))
# max = int(input('Введите максимальное значение '))
# from datetime import datetime
# dt = datetime.now()
# ran_numb =  dt.microsecond
# print(min + round(ran_numb / 1000000 * (max - min)))
# 
# 20.	Определить, присутствует ли в заданном списке строк, некоторое число.
#
# list = ['7 раз', 'отмерь', '1 раз', 'отрежь']
# n = input('Введите искомое число ')
# count = 0
# for i in range(len(list)):
#     for j in range(len(list[i]) - len(n)):
#         if list[i][j:j + len(n)] == n:
#             count += 1
# print(f'В заданном списке число {n} встречается {count} раз.')
#
# 21.	Определить позицию второго вхождения строки в списке либо сообщить, что её нет.
#       Примеры:
#       список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#       список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#       список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#       список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#       список: [], ищем: "123", ответ: -1
#
# list = ["123", "234", 123, "567"]
# string = "123"
# count = 0
# i = 0
# while i < len(list) and count < 2:
#     if list[i] == string:
#         count += 1
#     if count == 2:
#         print(f'Ответ: {i}')
#     i += 1
# if count < 2:
#     print('Ответ отрицательный.')
#
# 22.	Найти сумму чисел списка стоящих на нечетной позиции.
#
# import random
# list = []
# s = 0
# for i in range(random.randint(5, 15)):
#     list.append(random.randint(1, 10))
#     if i % 2 == 0:
#         s += list[i]
# print(list)
# print(f'Сумма чисел равна {s}')
#
# 23.	Найти произведение пар чисел в списке.
#       Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#       Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15].
# 
# import random
# list = []
# prod = []
# for i in range(random.randint(5, 20)):
#     list.append(random.randint(1, 50))
# for i in range(len(list)//2):
#     prod.append(list[i] * (list[len(list) - i - 1]))
# print(list)
# print(prod)
#
# 24.	В заданном списке вещественных чисел найдите разницу между 
#       максимальным и минимальным значением дробной части элементов.
#       Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#
# import random
# list = []
# max = 0
# min = 1
# for i in range(random.randint(5,15)):
#     num = round(random.random() * 10**random.randint(1,3), 2)
#     list.append(num)
#     if num - int(num) > max:
#         max = num - int(num)
#     if num - int(num) < min:
#         min = num - int(num)
# print(list)
# print(f'Разность максимальной и минимальной дробной части равна {round(max - min, 2)}')
#
# 25.	Написать программу преобразования десятичного числа в двоичное.
#
# num = int(input('Введите число '))
# binnum = ''
# while num != 0:
#     binnum = str(num%2) + binnum
#     num //= 2
# print(binnum) 
#
# 26.	Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
#    Т е для k = 8, список будет выглядеть так:
#    [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи.
#
# k = int(input('Укажите число k = '))
# fib = [1, 1]
# for i in range(2, k):
#     fib.append(fib[i-2] + fib[i-1])
# nonfib = [0, 1]
# for i in range(2, k+1):
#     nonfib.append(nonfib[i-2] - nonfib[i-1])
# for i in range(1, len(nonfib)):
#     nonfib.append(nonfib.pop(len(nonfib) - i - 1))
# print(nonfib + fib)
#

