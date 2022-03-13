# 41.	Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*.
#   Приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5; 
#   Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9.
#
# Без скобок:
#
# arithmetic = '123+15*5-45/9'
# data = arithmetic + ' '
# numbers = []
# sign = []
# num = ''
# for i in data:
#     if i.isdigit():
#         num += i
#     else:
#         numbers.append(int(num))
#         num = ''
#         sign.append(i)
# while '/' in sign:
#     sign_pos = sign.index('/')   
#     numbers.insert(sign_pos, numbers.pop(sign_pos) / numbers.pop(sign_pos))
#     sign.pop(sign_pos)
# while '*' in sign:
#     sign_pos = sign.index('*')   
#     numbers.insert(sign_pos, numbers.pop(sign_pos) * numbers.pop(sign_pos))
#     sign.pop(sign_pos)
# while '+' in sign:
#     sign_pos = sign.index('+')   
#     numbers.insert(sign_pos, numbers.pop(sign_pos) + numbers.pop(sign_pos))
#     sign.pop(sign_pos)
# while '-' in sign:
#     sign_pos = sign.index('-')   
#     numbers.insert(sign_pos, numbers.pop(sign_pos) - numbers.pop(sign_pos))
#     sign.pop(sign_pos)
# print(f'{arithmetic} = {numbers[0]}')
#
# Со скобками:
#
def calc(data): # Вычисения без скобок.
    data = data + ' '
    numbers = []
    sign = []
    num = ''
    for i in data:
        if i.isdigit():
            num += i
        else:
            numbers.append(int(num))
            num = ''
            sign.append(i)
    while '/' in sign:
        sign_pos = sign.index('/')   
        numbers.insert(sign_pos, numbers.pop(sign_pos) / numbers.pop(sign_pos))
        sign.pop(sign_pos)
    while '*' in sign:
        sign_pos = sign.index('*')   
        numbers.insert(sign_pos, numbers.pop(sign_pos) * numbers.pop(sign_pos))
        sign.pop(sign_pos)
    while '+' in sign:
        sign_pos = sign.index('+')   
        numbers.insert(sign_pos, numbers.pop(sign_pos) + numbers.pop(sign_pos))
        sign.pop(sign_pos)
    while '-' in sign:
        sign_pos = sign.index('-')   
        numbers.insert(sign_pos, numbers.pop(sign_pos) - numbers.pop(sign_pos))
        sign.pop(sign_pos)
    return numbers[0]

arithmetic = '(10*((2+8)*5+50)-200)/8+(15+25)/(20-16)'
while '(' in arithmetic:
    index_close = arithmetic.index(')')
    index_open = index_close - 1
    while arithmetic[index_open] != '(':
        index_open -= 1
    arithmetic = arithmetic[:index_open] + str(calc(arithmetic[index_open + 1: index_close])) + arithmetic[index_close + 1:]
print(calc(arithmetic))