# 33 Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена.
# Записать в файл многочлен степени k.

import random
list = []

def rand():                                 # Метод создания рандомного числа
    number = random.randint(0, 101)
    return number

def create_list(list):                      # Метод создания списка случайных коэффициентов
    values = 3
    while values > 0:
        list.append(rand())
        values = values - 1
    return list
print('Случайные коэффиценты:', create_list(list))

polynomial = f'{list[0]}x^2 + {list[1]}x + {list[2]}'
print('Сформированный многочлен:', polynomial)

with open('doc_33.txt', 'w') as data:        # Запись созданного многочлена в doc_33.txt
   data.write(polynomial)