# 39.	Игра: перед Вами 21 конфета. Вы берете по очереди от 1 до 3 конфет. Проигрывает тот, кто взял последнюю конфету.
#       Создайте такую игру для игры человек против человека.
#  a.	Добавьте игру против бота.
#  b.	Подумайте как наделить бота "интеллектом" .
#
bank = 21
count = 1
while bank > 1:
    if count%2:
        person = 'Игрок 1'
    else:
        person = 'Игрок 2'        
    bank -= int(input(f'{person}, Ваш ход '))
    print(f'Остлось {bank} конфет.')
    count += 1
if count%2:
    if bank == 1:
        print('Победил Игрок 2!')
    else:
        print("Игрок 2, you're a loser!")
else:
    if bank == 1:
        print('Победил Игрок 1!')
    else:
        print("Игрок 1, you're a loser!")
#
# Игрок против бота.
#
bank = 21
count = 1
import random
while bank > 1:
    if count%2:
        bank -= int(input('Игрок, Ваш ход '))
    else:
        move = random.randint(1,3) 
        print(f'Я взял {move} конфеты.') 
        bank -= move           
    print(f'Остлось {bank} конфет.')
    count += 1
if count%2:
    if bank == 1:
        print('Я победил!')
    else:
        print("I'm a loser!")
else:
    if bank == 1:
        print('Вы победили!')
    else:
        print("You're a loser!")    
#
# Игра с мудрецом.
#
bank = 21
count = 1
while bank > 1:
    if count%2:
        move1 = int(input('Игрок, Ваш ход '))
        bank -= move1
    else:
        move2 = 4 - move1 
        print(f'Я взял {move2} конфеты.') 
        bank -= move2           
    print(f'Остлось {bank} конфет.')
    count += 1
print('В следующий раз тебе повезет!')