"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from Lesson_3.array_functions import *


array = get_random_array(10, 1, 50)
max_ind = min_ind = 0
seg = []
seg_sum = 0

print(f'Исходный массив:\n{output_format(array)}')
for i, n in get_enumerator(array):
    if array[max_ind] < n:
        max_ind = i
    if array[min_ind] > n:
        min_ind = i

if max_ind < min_ind:
    max_ind, min_ind = min_ind, max_ind
print(f'Отрезок (индексация с 0): ({min_ind}, {max_ind})')

while min_ind < max_ind - 1:
    min_ind += 1
    seg_sum += array[min_ind]
    seg.append(array[min_ind])

print(f'sum({seg}) = {seg_sum}')


