# 14.	Подсчитать сумму цифр в вещественном числе.
#
import random
N = str(random.random()*100)
sum  = 0
for i in range(len(N)):
    if N[i].isdigit():
        sum += int(N[i])
print(f'Сумма цифр числа {N} равна {sum}')