# Задать список из N элементов, заполненных числами из [-N, N]
# Найти произведение элементов на указанных позициях
# Позиции хранятся в файле file.txt в одной строке одно число

with open('doc_17.txt','w') as data:
    data.write('0\n')
    data.write('1')

N = int(input('Введите число: '))
list = [x for x in range(-N, N+1)]
print(f'Дан список: {list}')

file = open('doc_17.txt', 'r')
result = 1
for i in file:
    index = i.replace('\n','')
    index = int(index)
    number = list[index]
    print('Числа в файле:', list[index])
    result *= number
print(f'Произведение элементов на указанных позициях = {result}')
file.close()