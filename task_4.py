# 4. Показать первую цифру дробной части числа

# Вариант 1
a = 3.923
b = (int (a * 10 % 10))
print(f'Первая цифра дробной части:',b)

# Вариант 2
c = 3.423
print(f'Первая цифра дробной части:',int(c * 10 % 10))