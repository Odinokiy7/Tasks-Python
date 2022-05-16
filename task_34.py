# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

list = []

# Создаем многочлен
polynomial_1 = f'{11}x^2 + {27}x + {34}'
print('Первый многочлен:', polynomial_1)
polynomial_2 = f'{32}x^2 + {16}x + {54}'
print('Второй многочлен:', polynomial_2)

# Записываем созданные многочлены в два новых файла
with open('doc_34_1.txt', 'w') as data:
   data.write(polynomial_1)
with open('doc_34_2.txt', 'w') as data:
   data.write(polynomial_2)

# Находим нужные индексы наших коэффицентов, прибавляем их и переводим в int значение
first_coef_polynomial_1 = int(polynomial_1[0] + polynomial_1[1])
second_coef_polinomial_1 = int(polynomial_1[8] + polynomial_1[9])
third_coef_polinomial_1 = int(polynomial_1[14] + polynomial_1[15])

first_coef_polynomial_2 = int(polynomial_2[0] + polynomial_2[1])
second_coef_polinomial_2 = int(polynomial_2[8] + polynomial_2[9])
third_coef_polinomial_2 = int(polynomial_2[14] + polynomial_2[15])

# Плюсуем найденные выше коэффиценты со своим значением
result1_coef = str(first_coef_polynomial_1 + first_coef_polynomial_2)
result2_coef = str(second_coef_polinomial_1 + second_coef_polinomial_2)
result3_coef = str(third_coef_polinomial_1 + third_coef_polinomial_2)

# Записываем новый файл txt, содержащий сумму созданных выше двух многочленов
result = f'{result1_coef}x^2 + {result2_coef}x + {result3_coef}'
with open('doc_34_result', 'w') as data:
    data.write(result)
print('Сумма многочленов:', result)