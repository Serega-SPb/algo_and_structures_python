"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

import random

START = 0
END = 50


def get_median(array, pos):

    if len(array) == 1:
        return array[0]

    pivot = random.choice(array)

    less = [x for x in array if x < pivot]
    more = [x for x in array if x > pivot]
    equal = [x for x in array if x == pivot]

    if len(less) > pos:
        return get_median(less, pos)
    elif len(less) + len(equal) > pos:
        return equal[0]
    else:
        return get_median(more, pos - len(less) - len(equal))


def main():
    m = int(input('Введите M: '))
    array = [random.randint(START, END) for _ in range(2*m + 1)]
    result = get_median(array, m)

    print(f'Исходный массив:\n{array}')
    print(f'Медиана: {result}')


if __name__ == '__main__':
    main()

"""
Введите M: 5
Исходный массив:
[24, 34, 24, 28, 25, 8, 10, 4, 44, 37, 31]
Медиана: 25
"""