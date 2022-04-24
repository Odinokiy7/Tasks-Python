# Найти максимальное из пяти чисел

array = [1, 62, 6, 41, 15]
max = array[0]
for count in array:
    if count > max:
        max = count
print(f'Максимальное число -', max)