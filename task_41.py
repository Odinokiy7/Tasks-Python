# 3 Реализуйте RLE алгоритм: Модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import count

with open('doc_41.txt', 'w') as data:
    #data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')
    data.write('AAAAAAAAAABAAAAAAAAAAAAAAAAAAAABBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBB')
    
with open('doc_41.txt', 'r') as data:
    string = data.readline()

count = 1
s = ""
for i in range(len(string)-1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            count += 1
        else:
            a = string[i]
            s+= str(count) + string[i]
            count = 1
s += str(count) + string[i]
print(s)

with open('doc_41_2.txt', 'w') as data:
    data.write(s)