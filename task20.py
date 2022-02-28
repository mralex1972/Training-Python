# 20.	Определить, присутствует ли в заданном списке строк, некоторое число.
#
list = ['7 раз', 'отмерь', '1 раз', 'отрежь']
n = input('Введите искомое число ')
count = 0
for i in range(len(list)):
    for j in range(len(list[i]) - len(n)):
        if list[i][j:j + len(n)] == n:
            count += 1
print(f'В заданном списке число {n} встречается {count} раз.')