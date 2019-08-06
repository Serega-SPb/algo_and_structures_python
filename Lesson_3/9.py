# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from Lesson_3.array_functions import *


ROWS = 5
COLUMNS = 5
matrix = []

for i in range(ROWS):
    array = get_random_array(COLUMNS, 1, 100)
    matrix.append(array)

min_values = []
for i in range(COLUMNS):
    min_val = None
    for j in range(ROWS):
        elem = matrix[j][i]
        if min_val is None:
            min_val = elem
            continue
        if min_val > elem:
            min_val = elem
    min_values.append(min_val)

result = min_values[0]
for n in min_values[1:]:
    if result < n:
        result = n

print('Исходная матрица')
for a in matrix:
    print(output_format(a))
print('-'*25)
print('Массив минимальных элементов столбцов')
print(output_format(min_values))
print('-'*25)
print('Максимальный элемент')
print(result)
