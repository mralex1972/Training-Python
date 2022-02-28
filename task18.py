# 18.	Реализовать алгоритм перемешивания списка.
#
list = [1,2,3,4,5,6,7,8,9,0]
import random
for i in range(len(list)):
    media = list[i]
    k = random.randint(1,len(list)-1)
    list[i] = list[k]
    list[k] = media
print(list)