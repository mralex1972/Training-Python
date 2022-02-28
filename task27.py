# 27.	Строка содержит набор чисел. Показать большее и меньшее число.
#       Символ-разделитель - пробел.
#
string = '12 345 6 7890 98 765 4 3210'
list = []
num = ''
for i in string:
    if i != ' ':
        num += i
    else:
        list.append(int(num))
        num = ''
max = list[0]
min = list[0]
for i in range(1,len(list)):
    if list[i] > max:
        max = list[i]
    if list[i] < min:
        min = list[i]
print(f'Наибольшее число в строке {max}\nНаименьшее число в строке {min}')