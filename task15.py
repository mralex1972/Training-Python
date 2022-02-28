# 15.	Написать программу получающую набор произведений чисел от 1 до N.
#  Пример: пусть N = 4, тогда[ 1, 2, 6, 24 ]
#
n = int(input('Введите N = '))
lst = []
lst.append(1)
for i in range(1,n):
    lst.append(lst[i-1] * (i+1))
print(lst)