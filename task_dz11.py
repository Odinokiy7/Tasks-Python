# Дана функция 'f(x) = -8x^2+3x+17'
# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

from sympy import *
import matplotlib.pyplot as plt

# 1. Определить корни
print('#1')
x = Symbol('x')
func = -8*x**2 + 3*x +17
y = solve(func)
x1 = float(y[0])
x2 = float(y[1])
print(x1, x2)

# 2. Найти интервалы, на которых функция возрастает
print('#2')
fd = diff(func)
print(solve(0<fd))


# 3. Найти интервалы, на которых функция убывает
print('#3')
print(solve(fd<0))


# 4. Построить график
print('#4')
list_y = []
for i in range(-5, 6):
    x = i
    y = -8*x**2 + 3*x +17
    list_y.append(y)
plt.plot(range(-5, 6), [0,0,0,0,0,0,0,0,0,0,0])
plt.plot(range(-5, 6), list_y)
plt.show()


# 5. Вычислить вершину
print('#5')
fd = diff(func)
corni = solve(fd)
top = corni[0]
x = top
y = -8*x**2 + 3*x +17
print(x, y)


# 6. Определить промежутки, на котором f > 0
print('#6')
print(solve(func>0))


# 7. Определить промежутки, на котором f < 0
print('#7')
print(solve(func<0))
