# 16. Задать список из n чисел последовательности (1+1/n)**n
# Вывести на экран их сумму

n = int(input('Введите число: '))
formula = [(1+1/i)**i for i in range(1, n)]
summa = round(sum(formula))
print(summa)