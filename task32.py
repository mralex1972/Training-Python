# 32.	Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности.
#       Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10].
#
import random
lst = []
result = []
for i in range(random.randint(10, 20)):
    lst.append(random.randint(1, 10))
resset = set(lst)
result = list(resset)
print(f'{lst} => {result}')