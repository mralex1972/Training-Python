# 16.	Задать список из n чисел последовательности (1+〖1/n)〗^n и вывести на экран их сумму.
#
list = []
n = int(input('Введите N '))
for i in range(1,n+1):
    list.append((1+ 1/i)**i)
print(list)
print(sum(list))
