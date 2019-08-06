#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from Lesson_3.array_functions import *


array = get_random_array(10, -10, 10)
max_neg = 0

for i in array:
    if i >= 0:
        continue

    if max_neg == 0:
        max_neg = i
    elif i > max_neg:
        max_neg = i

print(f'Исходный массив:\n{output_format(array)}')
print(f'Максимальный отрицательный элемент: {max_neg}')
