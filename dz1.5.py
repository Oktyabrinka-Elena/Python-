# Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# решение d = √ (х А – х В) 2 + (у А – у В) 2)

print ('Введите координаты точки X')
X1  = float(input('Введите X1: '))
X2  = float(input('Введите X2: '))
print ('Введите координаты точки Y')
Y1  = float(input('Введите Y1: '))
Y2  = float(input('Введите Y2: '))

result = ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5
print (result)
