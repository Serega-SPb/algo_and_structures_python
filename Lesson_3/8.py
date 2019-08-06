"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

from Lesson_3.array_functions import *


ROWS = 5
COLUMNS = 4
matrix = []


def array_sum(a):
    r = 0
    for i in a:
        r += i
    return r


for i in range(ROWS):
    array = get_random_array(COLUMNS-1, 1, 10)
    array.append(array_sum(array))
    matrix.append(array)

print('Итоговая матрица')
for a in matrix:
    print(output_format(a))
