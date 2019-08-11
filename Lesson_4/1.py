"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import random
import cProfile
from timeit import timeit


"""
L2-2 Посчитать четные и нечетные цифры введенного натурального числа.
Сравнение рекурсии и цикла (сложность O(n))
Скорость:
INPUT: 
Size: 10    Number: 10000
OUTPUT:
Loop:       0.32970349999999904
Recursion:  0.4401785999999994

INPUT: 
Size: 100    Number: 10000
OUTPUT:
Loop:       4.3700761
Recursion:  6.312509

Вывод: вариант с использованием цикла более эффективный по времени выполнения
"""


def l2_2_recursion(value):

    def shift(v, i=1, o=0, e=0):

        temp = v % (10 ** i) // (10 ** (i-1))

        if temp % 2 == 0:
            e += 1
        else:
            o += 1

        if v // (10 ** i) == 0:
            return o, e
        return shift(v, i + 1, o, e)

    odd_count, even_count = shift(value)
    return even_count, odd_count


def l2_2_loop(value):

    odd_count = 0
    even_count = 0

    # region i = len(value)
    i = 0
    while True:
        i += 1
        if value // (10 ** i) == 0:
            break
    # endregion

    i -= 1
    r = 0
    while i >= 0:
        value -= r
        temp = value // (10 ** i)
        r = temp * (10 ** i)

        if temp % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        i -= 1

    return even_count, odd_count


def tests():

    size = int(input('Size: '))
    value = int(''.join([str(random.randint(0, 10)) for i in range(size)]))
    print(value)

    print('Loop')
    cProfile.run(f'l2_2_loop({value})')
    print('='*50)
    print('Recursion')
    cProfile.run(f'l2_2_recursion({value})')
    print('=' * 50)

    count = int(input('Number: '))
    print('Loop')
    print(timeit(f'l2_2_loop({value})', setup='from __main__ import l2_2_loop', number=count))
    print('Recursion')
    print(timeit(f'l2_2_recursion({value})', setup='from __main__ import l2_2_recursion', number=count))

# ===========================================


def main():
    tests()


if __name__ == '__main__':
    main()
