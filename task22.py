# 22.	Найти сумму чисел списка стоящих на нечетной позиции.
#
import random
list = []
s = 0
for i in range(random.randint(5, 15)):
    list.append(random.randint(1, 10))
    if i % 2 == 0:
        s += list[i]
print(list)
print(f'Сумма чисел равна {s}')