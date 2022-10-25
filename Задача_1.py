# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141.  10-1 ≤ d ≤10-10

import math


d = float(input("точность: "))
sum = 0
a = 0
n = 0

while True:
    a = ((-1)**n)/(2*n+1)
    sum += a
    n += 1
    pi_new = sum*4
    if abs(a)*4 < d:
        break

print(f'Вычисленное значение Пи (формула Лейбница) = {pi_new}')
print(f'Пи из библиотеки math: {math.pi}')