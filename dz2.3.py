# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
from msilib import sequence

N = int(input('Введите число: ')) 

def get_squerence(N):
    return [round((1 + 1 / x)**x, 5) for x in range (1, N + 1)]

nums = get_squerence(N)
print(nums)
print(round(sum(nums), 5))