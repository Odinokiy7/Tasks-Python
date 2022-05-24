# 14. Подсчитать сумму цифр в вещественном числе.

# Вариант 1
# import random
# number = random.uniform(1, 1001)       # задаем случайное вещественное число
# print('Задано число:', number)
# number = str(number).replace('.', '')  # переводим в строковый тип, убираем точку
# print('Получили число:', number)
# result = sum(map(int, number))         # переводим в числовой тип, считаем сумму
# print('Сумма цифр данного числа =', result)

# Вариант 2 с использованием MAP
number = 123.456
result = sum(map(int, str(number).replace('.', '')))
print(f'Дано вещественное число: {number}\nСумма всех цифр в числе = {result}')