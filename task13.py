# 13.	Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
#
text = input('Введите исследуемый текст \n')
search_text = input('Введите искомый текст \n')
count = 0
for i in range(len(text)-len(search_text)):
    if text[i:i+len(search_text)] == search_text:
        count += 1
print(f'Искомый текст найден {count} раз.')