"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from Lesson_3.array_functions import *


array = get_random_array(10, 1, 50)
sort_array = get_sorted(array)
result = sort_array[:2]

print(f'Исходный массив:\n{output_format(array)}')
print(f'Два наименьших элемента:\n{output_format(result)}')
