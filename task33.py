# 33.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#       многочлена и записать в файл многочлен степени k. 
#       *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0.

k = int(input('Укажите степень многочлена k = '))
import random
data = open('multicock.txt', 'a')
multiplier = str(random.randint(1,10))
if multiplier == '1':
    multiplier = ''
data.writelines(f'{multiplier}X^{k}')
for i in range(k-1, -1, -1):    
    multiplier = random.randint(-10, 10)
    mon = ''
    if multiplier != 0:        
        if multiplier > 1:
            mon += ' + ' + str(multiplier)
        if multiplier < -1:
            mon += ' - ' + str(abs(multiplier))
        if multiplier == 1:
            mon += ' + '  
        if multiplier == -1:
            if i == 0:
                mon += ' -1 '
            mon += ' - '
        if i > 0:
            mon += 'X'
        if i > 1:
            mon += '^'+ str(i)
    data.writelines(mon)
data.close()