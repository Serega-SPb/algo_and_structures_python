"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import random
from Lesson_7.sort_functions import merge_sort, merge_sort_parallel

START = 0
END = 50


def main():
    size = int(input('Введите длину массива: '))
    array = [round(random.uniform(START, END), 2) for _ in range(size)]
    sorted_array = merge_sort(array.copy())
    print(f'Исходный массив:\n{array}')
    print(f'Отсортированный массив:\n{sorted_array}')


if __name__ == '__main__':
    main()

"""
Введите длину массива: 10
Исходный массив:
[10.9, 25.25, 6.09, 34.49, 46.21, 11.15, 1.73, 25.06, 40.73, 22.03]
Отсортированный массив:
[1.73, 6.09, 10.9, 11.15, 22.03, 25.06, 25.25, 34.49, 40.73, 46.21]
"""