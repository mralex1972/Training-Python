# 24.	В заданном списке вещественных чисел найдите разницу между 
#       максимальным и минимальным значением дробной части элементов.
#       Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#
import random
list = []
max = 0
min = 1
for i in range(random.randint(5,15)):
    num = round(random.random() * 10**random.randint(1,3), 2)
    list.append(num)
    if num - int(num) > max:
        max = num - int(num)
    if num - int(num) < min:
        min = num - int(num)
print(list)
print(f'Разность максимальной и минимальной дробной части равна {round(max - min, 2)}')