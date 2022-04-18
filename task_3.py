# 3. Вывести на экран числа от -N до N

# Мое решение
n = [-3, -2, -1, 0, 1, 2, 3]
print(n)

# Решение с семинара
n = int(input('Введите число: '))
for count in range(-n, n+1):
    print(count, end=' ')