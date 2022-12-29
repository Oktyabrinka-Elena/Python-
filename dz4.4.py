# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = int(input('Задайте натуральную степень k: '))
import File4_1 as cp 
coeff_polynom = cp.fill_coefficients_polynomial_list(k)
my_file = 'f_polinom4_4.txt'
import File4_2 as fc
fc.call_record_func(k, coeff_polynom, my_file)