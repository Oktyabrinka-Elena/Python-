# Вычислить число pi c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
from math import pi

Num = pi
# print(Num)

# Формула Бэйли-Боруэйна-Плаффа 10^(-1) <= d10 <= 10^(-10)

Num = 100
pi_N = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(Num))

print(pi_N)