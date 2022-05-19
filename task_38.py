# Напишите программу, которая удаляет из текста все слова, содержащие "абв"

text = 'абвтекст текст абвтекст2 текст2'
print('text:', text)

# Делим строку на слова
text_word = text.split()
print('text_word:', text_word)

# Фрагмент, по которому будем удалять слова
find = 'абв'

# Новый список для оставшихся слов
new_text = []

# Проверяем, если в слове нет сочетания "абв" - добавляем его в новый список
for i in text_word:
    if find not in i:
        new_text.append(i)
print('new_text:', new_text)

# Сбор новой строки через /join разделитель - пробел
text_2 = ' '.join(new_text)
print('Вывод:', text_2)