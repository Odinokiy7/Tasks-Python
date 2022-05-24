# 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1
# Пример: для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# Вариант 1
# slovar = {}
# n = int(input('n = '))
# for i in range(1, n+1):
#     slovar[i] = 3 * i + 1
# print(slovar)

# Вариант 2 с использованием LIST COMPREHENSION
dictionary = {n:3*n+1 for n in range (1,7)}
print (dictionary)