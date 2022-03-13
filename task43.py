#  43.	Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#   Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10].
#
import random
lst = []
for i in range(random.randint(10,20)):
    lst.append(random.randint(1,11))
print(lst)
lst2 = list(set(lst))
for e in lst2:
    lst.pop(lst.index(e))
lst3 = list(filter(lambda x: not(x in lst), lst2))
print(lst3)