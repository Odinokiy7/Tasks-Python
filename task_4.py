# Показать первую цифру дробной части числа

# Вариант 1
number = 123.987
result = int(number * 10 % 10)
print(f'Первая цифра дробной части:',result)

# Вариант 2
count = 321.012
print(f'Первая цифра дробной части:',int(count * 10 % 10))