# Вывести на экран числа от -N до N

N = int(input('Введите число: '))
for count in range(-N, N + 1):
    print(count, end=' ')