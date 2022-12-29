# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

K = int(input('Введите значение: '))

def Fibonacci (K):
    fibonacci_arr = []
    a, b = 1, 1
    for i in range(K-1):
        fibonacci_arr.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (K):
        fibonacci_arr.insert(0, a)
        a, b = b, a - b
    return fibonacci_arr

fibonacci_arr = Fibonacci (K)
print(Fibonacci (K))
print(fibonacci_arr.index(0))