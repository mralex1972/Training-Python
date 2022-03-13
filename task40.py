# Крестики-нолики.
#
def det_of_vic(lst): # Отслеживает факт выигрыша
    global vic
    for x in range(1,4):
        count = 0
        for y in range(1,4):
            if (x,y) in lst:
                count += 1
        if count == 3:
            print(f'Выиграл {name}')
            vic = 'Победа'
    for y in range(1,4):
        count = 0
        for x in range(1,4):
            if (x,y) in lst:
                count += 1
        if count == 3:
            print(f'Выиграл {name}')
            vic = 'Победа'
    count = 0
    for i in range(1,4):
        if (i,i) in lst:
            count += 1
    if count == 3:
            print(f'Выиграл {name}')
            vic = 'Победа'
    count = 0
    for i in range(1,4):
        if (i,4-i) in lst:
            count += 1
    if count == 3:
            print(f'Выиграл {name}')
            vic = 'Победа'
import os
os.system('cls')
string = ['   |   |   ', '   |   |   ', '   |   |   ']
print(string[0])
print('---|---|---')
print(string[1])
print('---|---|---')
print(string[2])
X = [] # У меня все ходы записаны!
O = []
vic = ''
turn = 1
while len(X) + len(O) < 9 and vic == '': # Условие предоставления следующего хода
    if turn%2:
        name = 'X'
    else:
        name = 'O'
    print(f'Ходит {name}.\nУкажите столбец и строку ')
    x = 0
    y = 0
    while not(0<x<4 and 0<y<4) or ((x,y) in X or (x,y) in O): # Проверка вводимых значений
        x = int(input('Столбец:   '))
        y = int(input('Строка:   '))
    if turn%2:
        X.append((x,y))
    else:
        O.append((x,y)) 
# Графическое отображение хода: 
    list = []  
    for i in range(len(string[y-1])):
        if i == 1+4*(x-1):
            list.append(name)
        else:
            list.append(string[y-1][i])
    string[y-1] = ''
    for i in range(len(list)):
        string[y-1] += list[i]             
    os.system('cls')    
    print(string[0])
    print('---|---|---')
    print(string[1])
    print('---|---|---')
    print(string[2])
    if turn%2:
        det_of_vic(X)
    else:
        det_of_vic(O)
    turn +=1
if vic == '':
    print('Ничья!')