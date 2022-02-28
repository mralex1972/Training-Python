# 37.	Дан список чисел. Создать список в который попадают числа, описывающие возрастающую
#  последовательность и содержащие максимальное количество элементов.
#  Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#   [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7].
#
import random
lst = []
for i in range(random.randint(7, 15)):
    lst.append(random.randint(1, 10))    
print(lst)
res = []
def dif_ideal_value(index):
    return abs(lst[index] - float(10/len(lst)*(index + 1)))
res.append((lst[0], dif_ideal_value(0)))
for i in range(1, len(lst)):
    res.append((lst[i], dif_ideal_value(i)))    
    while res[len(res)-1][0] <= res[len(res)-2][0] and len(res) > 1:
       if res[len(res)-1][1] > res[len(res)-2][1]:
           res.pop()
       else:
            res.pop(len(res)-2)
result = []
for i in range(len(res)):
    result.append(res[i][0])
print(result)