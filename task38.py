# 38.	Напишите программу, удаляющую из текста все слова, содержащие "абв".
#
text = 'Пусть абвгдe будет солнце, Пусть абвгдe будет небо, Пусть абвгдe будет мама, Пусть абвгдe буду я'
taboo = 'абв'
censor = ''
word = ''
text_with_space = text + ' '
for letter in text_with_space:    
    word += letter
    if letter == ' ':        
        if taboo not in word:
            censor += word
        word = ' '   
print(censor)