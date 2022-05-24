# 11. Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
# Вариант 1
# list = []
# N = int(input('Введите количество членов последовательности: '))
# for i in range(N):
#     if i % 2 == 0:
#         list.append(3**i)
#     else:
#         list.append(-3**i)
# print(list)

# Вариант 2
# import os
# os.system("cls")

# def sub (x):
#     if x in [0,1]:
#         return 1
#     else:
#         return sub (x-1)*-3
# list = []
# for N in range (1,10):
#     list.append (sub(N)) # Добавление элемента в конец списка
# print (list)

# Вариант 3
# count = int(input('Введите количество элементов: '))
# num = 1
# list = [1]
# for i in range (0, count - 1):
#     num *= -3
#     list.append(num)
# print(list)


# Вариант 4 с использованием LIST COMPREHENSION
result = [(-3)**x for x in range(0, 5)]
print(result)