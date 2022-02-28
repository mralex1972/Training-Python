# 34.	Даны два файла в каждом из которых находится запись многочлена.
#    Сформировать файл содержащий сумму многочленов.
#
# Считывание строки из файла:
def string(path):
    data = open(path, 'r')
    string = ''
    for line in data:
        string += line 
    return string
# Определение степени многочлена:
def exp(path):
    mistring = string(path)       
    i = 0
    while mistring[i] != 'X':
        i += 1
    k = i+2
    expon = ''
    while mistring[k].isdigit():
        expon += mistring[k]
        k += 1
    return int(expon)
if exp('multicock1.txt') > exp('multicock2.txt'):
    ex = exp('multicock1.txt')
else:
    ex = exp('multicock2.txt')
# Анализ многочлена
data1 = string('multicock1.txt')
data2 = string('multicock2.txt')
def coeflist(data, ex):
# Список, заполненный 0, длиной наибольшей степени многочлена
#  для дальнейшего заполнения коэффициентами:
    cfcnts = []
    for j in range(ex + 1):
        cfcnts.append(0)
# Старший коэффициент: 
    if  data[0] + data[1] == 'X^':
        cfcnts[len(data)-1] = 1
    elif data[0] + data[1] == '-X':
        cfcnts[len(data)-1] = -1
    else:
        n = 0
        coef1 = ''
        while data[n] != 'X':
            coef1 += data[n]
            n += 1
        cfcnts[len(data)-1] = int(coef1)
# Следующие коэффициенты:    
    for i in range(4, len(data)-2):
        if data[i]+data[i+1] == 'X^':
            def cfcnt(data, i):
                k = 1
                coef = ''
                while data[i-k].isdigit():
                    coef = data[i-k] + coef
                    k += 1
                if coef == ' ':
                    coef = '1'
                if data[i-k-1] == '-':
                    return int(coef)*(-1)
                else:
                    return int(coef) 
# Индекс коэффициента в списке:
            ind = ''
            k = 2
            while data[i+k].isdigit():
                ind += data[i+k]
                k += 1
            cfcnts[int(ind)]=cfcnt(data, i)
# Поиск Х после нахождения последнего Х^ в строке:
            ii = i # индекс последнего вхождения Х^
    i = ii + 6
    while data[i] != 'X':
        i += 1
    cfcnts[1]=cfcnt(data, i)
# Нахождение свободного члена:
    if data[ex] == 'X' or (data[ex].isdigit() and data[ex - 1] == '^'):
        cfcnts[0] = 0
    else:
        coef = int(data[ex-1, 2])
        if data[ex - 4, 3].find('+') == -1:
            coef *= -1
    cfcnts[0] = coef
    return cfcnts
coeflist1 = coeflist(data1, ex)
coeflist2 = coeflist(data2, ex)
coef_sum_list = []
# Создание списка коэффициентов суммы:
for i in range(ex + 1):
    coef_sum_list.append(coeflist1[i] + coeflist2[i])
# Создание записи в файл:
polynom = open('polynom.txt', 'a')
for i in range(len(coef_sum_list)):
    multiplier = coef_sum_list[i]
    mon = ''
    if multiplier != 0:
        if multiplier > 1:
            mon += ' + ' + str(multiplier)
        if multiplier < -1:
            mon += ' - ' + str(abs(multiplier))
        if multiplier == 1 and i != len(coef_sum_list) - 1:
            mon += ' + '
        if multiplier == -1:
            if i == 0:
                mon += ' - 1'
            mon += ' - '
        if i > 0:
            mon += 'X'
        if i > 1:
            mon += '^' + str(i)
    polynom.writelines(mon)
polynom.close()