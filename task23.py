# 23.	Найти произведение пар чисел в списке.
#       Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#       Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15].
# 
import random
list = []
prod = []
for i in range(random.randint(5, 20)):
    list.append(random.randint(1, 50))
for i in range(len(list)//2):
    prod.append(list[i] * (list[len(list) - i - 1]))
print(list)
print(prod)