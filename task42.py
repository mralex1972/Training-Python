# 42.	Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# a.	входные и выходные данные хранятся в отдельных текстовых файлах
#
# Сжатие data42 в RLEdata42:

f = open('data42.txt', 'r')
data = f.read() + ' '
RLEdata = open('RLEdata42.txt', 'a')
count = 1
for i in range(1,len(data)):
    if data[i] == data[i-1]:
        count += 1
    else:
        RLEdata.write(f'{data[i-1]},{count} ')
        count = 1
f.close()
RLEdata.close()

# Восстановление RLEdata42 в retrieved_data42:

f = open('RLEdata42.txt','r')
data = f.read()
retrieved_data = open('retrieved_data42.txt','a')
for i in range(1,len(data)):
    if data[i] == ',':
        n = ''
        symbol = data[i-1]
    elif data[i] != ' ':
        n+=data[i]
    else:
        for j in range(int(n)):
            retrieved_data.write(f'{symbol}')
f.close()
retrieved_data.close()
