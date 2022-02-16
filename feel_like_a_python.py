# 1. По двум заданным числам проверять является ли первое квадратом второго.
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
# 2. Даны два числа. Показать большее и меньшее число.
#
# a = int(input('введите число '))
# b = int(input('введите число снова '))
# if a > b:
#     print(f'Наибольшее {a}')
# elif a < b:
#     print(f'Наибольшее {b}')
# else:
#     print('Числа равны')
#
# 3. По заданному номеру дня недели вывести его название.
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
# 4. Найти максимальное из трех чисел.
#
# list = []
# for i in range(3):
#      print('Введите число')
#      list.append(input()) 
# max = list[0]
# for j in range(1,3):
#     if list[j] > max:
#         max = list[j]
# print(f'Максимальное значение {max}')
#
# 5. Написать программу вычисления значения функции y = f(a).
#
# def f(x):
#     print('y = f(x)')
#     return
#
# 6. Выяснить является ли число чётным.
#
# N = int(input('Введите число  '))
# if N % 2:
#     print(f'{N} - нечетное число')
# else:
#     print(f'{N} - четное число')
#
# 7. Показать числа от -N до N.
#
# n = int(input('Введите N  '))
# for i in range(-n,n+1):
#     print(i)
#
# 8. Показать четные числа от 1 до N.
#
# N = int(input('Введите N  '))
# for i in range(2,N+1,2):
#     print(i)
#
# 9. Показать последнюю цифру трёхзначного числа.
#
# print('Введите трехзначное число')
# num = input()
# if len(num) == 3:
#     print(num[2])
# else:
#     print('Я же просил трехзначное число!')
#
# 10. Показать вторую цифру трёхзначного числа.
#
# print('Введите трехзначное число')
# num = input()
# if len(num) == 3:
#     print(num[1])
# else:
#     print('Я же просил трехзначное число!')
#
# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа.
#
# N = input('Введите число из отрезка [10, 99]  ')
# if len(N) == 2:
#     if N[0] > N[1]:
#         print(f'Наибольшая цифра {N[0]}')
#     elif N[1] > N[0]:
#         print(f'Наибольшая цифра {N[1]}')
#     else:
#         print('Цифры равны.')
# else:
#     print('Число не принадлежит отрезку [10, 99]')
#
# 12. Удалить вторую цифру трёхзначного числа.
#
# print('Введите трехзначное число')
# num = input()
# if len(num) == 3:
#     print(num[0] + num[2])
# else:
#     print('Я же просил трехзначное число!')
#
# 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.
#
# divident = int(input('Введите делимое  '))
# divider = int(input('Введите делитель  '))
# rem = divident % divider
# if rem == 0:
#     print('Кратно!')
# else:
#     print(f'Остаток деления равен {rem}')
#
# 14. Найти третью цифру числа или сообщить, что её нет.
#
# num = input('Введите число  ')
# if len(num) < 3:
#     print('Нет такой цифры в этом числе!')
# else:
#     print(f'Нашел!  {num[2]}')
# #
# 15. Дано число. Проверить кратно ли оно 7 и 23.
#
# num = int(input('Введите число  '))
# if num % 7 == 0 and num % 23 == 0:
#     print('Кратно!')
# else:
#     print('Не кратно!')
#
# 16. Дано число обозначающее день недели. Выяснить является номер дня недели выходным.
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
# 17. По двум заданным числам проверять является ли одно квадратом другого.
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
# 18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y.

# for x in range(0,2):
#     for y in range(0,2):
#         if not(x or y) == ((not x) and (not y)):
#             print(f'При X = {x}  Y = {y}    Истинно')
#         else:
#             print(f'При X = {x}  Y = {y}    Ложь')

# 19. Определить номер четверти плоскости, в которой находится точка
#  с координатами Х и У, причем X ≠ 0 и Y ≠ 0.
#
# x = int(input('Введите координату Х  '))
# y = int(input('Введите координату Y  '))
# if y > 0:
#     if x > 0:
#         print('I четверть')
#     else:
#         print('II четверть')
# else:
#     if x > 0:
#         print('IV четверть')
#     else:
#         print('III четверть')
#
# 20. Задать номер четверти, показать диапазоны для возможных координат.
# #
# coord = ['X>0 ; Y>0', 'X<0 ; Y>0', 'X<0 ; Y<0', 'X>0 ; Y<0']
# quarter = int(input('Введите номер четверти  '))
# if 0<quarter<5:
#     print(coord[quarter - 1])
# else:
#     print('Шутник!')
# #
# 21. Программа проверяет пятизначное число на палиндромом.
#
# print('Введиье пятизначное число')
# num = input()
# res = 1
# if len(num) == 5:
#     for i in range(len(num)//2):
#         if num[i] != num[4-i]:
#             res = 0
#     if res:
#         print('Палиндром')
#     else:
#         print('Не палиндром')
# else:
#     print(f'Я же просил пятизначное число, а тут {len(num)} цифр')
#
# 22. Найти расстояние между точками в пространстве 2D/3D.
# (3D)
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
# #
# # (2D)
# #
# print('Введите координаты точек (X1;Y1) и (X2;Y2)')
# x1 = float(input('X1 = '))
# y1 = float(input('Y1 = '))
# x2 = float(input('X2 = '))
# y2 = float(input('Y2 = '))
# dx = x2 - x1
# dy = y2 - y1
# print(f'Расстояние между точками равно {round((dx**2 + dy**2)**0.5, 2)}')
#
# 23. Показать таблицу квадратов чисел от 1 до N.
#
# print('Введите N')
# n = int(input())
# for i in range(1,n+1):
#     print(f'{i}^2 = {i**2}')
#
# 24. Найти кубы чисел от 1 до N.
#
# print('Введите N')
# n = int(input())
# for i in range(1,n+1):
#     print(f'{i}^3 = {i**3}')
# 
# 25. Найти сумму чисел от 1 до А.
#
# print('Введите A')
# a = int(input())
# s = 0
# for i in range(1,a+1):
#     s += i
# print(f'Сумма чисел от 1 до {a} равна {s}')
#
# 26. Возведите число А в натуральную степень B используя цикл.
# 
# a = int(input('Введите основание степени А = '))
# b = int(input('Введите показатель степени В = '))
# s = 1
# for i in range(b):
#     s= s * a
# print(f'{a}^{b} = {s}')
#
# 27. Определить количество цифр в числе.
#
# num = input('Удиви меня своим числом ')
# print(f'В этом числе {len(num)} цифр.')
#
# 28. Подсчитать сумму цифр в числе.
#
# num = input('Удиви меня своим числом ')
# s = 0
# for i in range(len(num)):
#     s += int(num[i])
# print(f'Сумма цифр в этом числе равна {s}')
#
# 29. Написать программу вычисления произведения чисел от 1 до N.
#
# n = int(input('Введите N = '))
# p = 1
# for i in range(n):
#     p *= i+1
# print(f'Произведение равно {p}')
#
# 30. Показать кубы чисел, заканчивающихся на четную цифру.
#
# n = int(input('Укажите максимальное число '))
# for i in range(1,n+1):
#     if not(i**3 % 2) and i**3%10 != 0:
#         print(f'{i}^3 = {i**3}')
# #
# 31. Задать массив из 8 элементов и вывести их на экран.
#
# elements = []
# for i in range(8):
#     elements. append(input('Введите что-нибудь '))
# print(elements)
#
# 32. Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран.
#
# import random
# zerone = []
# for i in range(8):
#     zerone.append(random.randint(0,1))
# print(zerone)
#
# 33. Задать массив из 12 элементов, заполненных числами из [-9,9].
#  Найти сумму положительных/отрицательных элементов массива.
#
# import random
# list = []
# sumpos = 0
# sumneg = 0
# for i in range(12):
#     list.append(random.randint(-9,9))
#     if list[i] > 0:
#         sumpos += list[i]
#     else:
#         sumneg += list[i]
# print(list)
# print(f'Сумма положительных элементов {sumpos}')
# print(f'Сумма отрицательных элементов {sumneg}')
#
# 34. Написать программу замену элементов массива на противоположные.
#
# import random
# def invers(list):
#     for i in range(len(list)):
#         list.insert(i,- list.pop(i))
# list = []
# for k in range(random.randint(5,15)):
#     list.append(random.randint(-100,100))
# print(list)
# invers(list)
# print(list)
#      
# 35. Определить, присутствует ли в заданном массиве, некоторое число.
#
# import random
# list = []
# for k in range(10):
#     list.append(random.randint(1,20))
# print('Я загадал 10 чисел от 1 до 20')
# N = int(input('Угадай число '))
# count = 0
# for i in range(len(list)):
#     if list[i] == N:
#         count +=1
# if count == 0:
#     print('Нет такой буквы в этом слове! ')
# else:
#     print(f'В этом слове {N} присутствует {count} раз!  ')
# print(list)
#
# 36. Задать массив, заполнить случайными положительными трёхзначными числами.
#  Показать количество нечетных\четных чисел.
#
# import random
# list = []
# count_even = 0
# count_odd = 0
# for k in range(10):
#     list.append(random.randint(100,999))
#     if list[k] % 2:
#         count_odd += 1
#     else:
#         count_even += 1
# print(list)
# print(f'Количество четных {count_even}')
# print(f'Количество нечетных {count_odd}')
#
# 37. В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99].
#
# import random
# list = []
# count = 0
# for i in range(123):
#     list.append(random.randint(1,500))
#     if 9 < list[i] < 100:
#         count += 1
# print(list)
# print(f'В списке {count} чисел из отрезка [10,99]')
#
# 38. Найти сумму чисел одномерного массива стоящих на нечетной позиции.
#
# import random
# list = []
# sum = 0
# for i in range(10):
#     list.append(random.randint(1,10))
#     if i % 2 != 1:
#         sum += list[i]
# print(list)
# print(f'Сумма членов на нечетных позициях {sum}')
#
# 39. Найти произведение пар чисел в одномерном массиве.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# import random
# list = []
# for i in range(random.randint(5,20)):
#     list.append(random.randint(1,10))
# print(list)
# for i in range(len(list)//2):
#     print(f'{list[i]} * {list[len(list) - i - 1]} = {list[i] * list[len(list) - i - 1]}')
#
# 40. В Указанном массиве вещественных чисел найдите разницу между максимальным и
#  минимальным элементом.
#
# import random
# list = []
# for i in range(random.randint(5,20)):
#     list.append(random.random()*100)
# max = list[0]
# min = list[0]
# for i in range(1, len(list)):
#     if list[i] > max:
#         max = list[i]
#     elif list[i] < min:
#         min = list[i]
# print(list)
# print(f'Разница между максимальным и минимальным {max - min}')
#
# 41. Выяснить являются ли три числа сторонами треугольника.
#
# print('Введите 3 числа ')
# a = int(input())
# b = int(input())
# c = int(input())
# if a < b+c and b < a + c and c < a + b:
#     print(f'Числа {a}, {b}, {c} являются длинами сторон треугольника.')
# else:
#     print(f'Числа {a}, {b}, {c} не являются длинами сторон треугольника.')
#
# 42. Определить сколько чисел больше 0 введено с клавиатуры.
#
# print("Введите число \n Для завершения нажмите ENTER")
# count = 0
# symbol = input()
# while symbol != '':
#     if symbol.isdigit():
#         if int(symbol) > 0:
#             count += 1
#     symbol = input()
# print(f'Вы ввели {count} положительных чисел.')
#
# 43. Написать программу преобразования десятичного числа в двоичное.
#
# num = int(input('Введите число '))
# binnum = ''
# while num != 0:
#     binnum = str(num%2) + binnum
#     num //= 2
# print(binnum) 
#
# 44. Найти точку пересечения двух прямых заданных уравнением
#  y = k1 * x + b1, y = k2 * x + b2, b1 k1 и b2 и k2 заданы.
#
# print('Введите k1 и b1 для первой прямой.')
# k1 = float(input('k1 = '))
# b1 = float(input('b1 = '))
# print('Введите k2 и b2 для второй прямой.')
# k2 = float(input('k2 = '))
# b2 = float(input('b2 = '))
# if k1 == k2:
#     if b1 == b2:
#         print('Прямые совпадают.')
#     else:
#         print('Прямые параллельны.')
# else:
#     print(f'Прямые пересекаются в точке ({round((b2 - b1)/(k1 - k2), 2)} ; {round((k1*b2 - k2*b1)/(k1 - k2), 2)})')
#
# 45. Показать числа Фибоначчи.
#
# n = int(input('Укажите число элементов последовательности '))
# fib = [1, 1]
# for i in range(2, n):
#     fib.append(fib[i-2] + fib[i-1])
# print(fib)
#
# 