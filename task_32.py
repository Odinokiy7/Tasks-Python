# 32 Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

1
list = [1, 3, 5, 4, 9, 14, 5, 1]
print(list)
list_empty = []
for i in range (0, len(list)):
    count = 0
    for j in range (0, len(list)):
        if i != j:
            if list[i] == list[j]:
                count = 1
    if count == 0:
        list_empty.append(list[i])
print(list_empty)



# 2
# list = list(map(int,input('Введите последовательность чисел через пробел:').split()))
# print('Список неповторяющихся элементов исходной последовательности:', set(list))