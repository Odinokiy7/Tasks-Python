# Вычислить число 'п' c заданной точностью d

import math
P = 0.001
#P = float(input("Введите количество знаков после запятой для вычисления числа Пи (от 1 до 10 ):\n"))
P = str(P).split('.')
L = len(P[1])
M = str(math.pi)
print(float(M[:L+2]))
