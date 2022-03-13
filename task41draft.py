# 41.	Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*.
#   Приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5; 
#   Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9.
#


# Со скобками:

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
def parent_calc(data): # Разбирается в скобках.
    if '(' in data:    
        count = 1        
        index_open = data.index('(')
        index_close = index_open
        while count > 0:
            index_close += 1
            if data[index_close] == '(':
                count += 1
            elif data[index_close] == ')':
                count -= 1            
        parent_calc(data[index_open + 1: index_close])
    else:
        data = data[:index_open] + str(calc(data[index_open + 1: index_close])) + data[index_close+1:]
arithmetic = '(10*(2+8)+50)*2+(15+25)/(20-16)'   
while '(' in arithmetic:
    parent_calc(arithmetic)
calc(arithmetic)
