# 17.	Задать список из N элементов, заполненных числами из [-N, N].
#    Найти произведение элементов на указанных позициях.
#    Позиции хранятся в файле file.txt в одной строке одно число.
#
n = int(input('Введите N '))
list = []
for i in range(2*n + 1):
    list.append(i - n)
print(list)
data = open('file.txt', 'a')
import random
# Записываем в файл случайное количество случайных значений индексов
# элементов списка:
for i in range(2, random.randint(3, 2*n + 1)):
    num = random.randint(0, 2*n)
    data.writelines(f'{num}\n')
data.close()
data = open('file.txt', 'r')
p = 1
for line in data:
    index = int(line)
    p *= list[index]
print(f'Произведение элементов равно {p}')
data.close()