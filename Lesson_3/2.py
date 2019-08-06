"""
2.	Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

from Lesson_3.array_functions import *


first_array = get_random_array(10, 1, 50)
second_array = []

for i, n in get_enumerator(first_array):
    if n % 2 == 0:
        second_array.append(i)

# Для индексации с 1
# for i, n in get_enumerator(first_array, 1):
#     if n % 2 == 0:
#         second_array.append(i)

print(f'Исходный массив:\n{first_array}')
print(f'Индексы четных элементов (индексация с 0):\n{second_array}')
