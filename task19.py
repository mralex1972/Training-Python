# 19.	Реализовать алгоритм задания случайных чисел.
#   Без использования встроенного генератора псевдослучайных чисел.
#
min = int(input('Введите минимальное значение '))
max = int(input('Введите максимальное значение '))
from datetime import datetime
dt = datetime.now()
ran_numb =  dt.microsecond
print(min + round(ran_numb / 1000000 * (max - min)))