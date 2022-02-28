# 2.	Найти максимальное из пяти чисел.
#
list = [5,6,9,8,7]
for i in range(5):
     print('Введите число')
     list[i] = int(input())
max = list[0]
for j in range(1,5):
    if list[j] > max:
        max = list[j]
print(f'Максимальное значение {max}')