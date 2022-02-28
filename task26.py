# 26.	Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
#    Т е для k = 8, список будет выглядеть так:
#    [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи.
k = int(input('Укажите число k = '))
fib = [1, 1]
for i in range(2, k):
    fib.append(fib[i-2] + fib[i-1])
nonfib = [0, 1]
for i in range(2, k+1):
    nonfib.append(nonfib[i-2] - nonfib[i-1])
for i in range(1, len(nonfib)):
    nonfib.append(nonfib.pop(len(nonfib) - i - 1))
print(nonfib + fib)