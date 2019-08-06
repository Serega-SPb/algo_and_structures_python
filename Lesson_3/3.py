#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from Lesson_3.array_functions import *


rand_array = get_random_array(10, 1, 50)
max_ind = min_ind = 0

print(f'Исходный массив:\n{output_format(rand_array)}')

for i, n in get_enumerator(rand_array):
    if rand_array[max_ind] < n:
        max_ind = i
    if rand_array[min_ind] > n:
        min_ind = i

rand_array[min_ind], rand_array[max_ind] = rand_array[max_ind], rand_array[min_ind]
print(f'Получившийся массив:\n{output_format(rand_array)}')
