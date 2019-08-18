"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

import sys
import random
from memory_profiler import profile
from Lesson_6.sieve_eratosthenes import *
from Lesson_6.les2_2 import *

P = 5


@profile(precision=P)
def se_e(n):
    return sieve_eratosthenes_exm(n)


@profile(precision=P)
def se(n):
    return sieve_eratosthenes(n)


@profile(precision=P)
def bf(n):
    return brute_force(n)


@profile(precision=P)
def recur(v):
    return recursion(v)


@profile(precision=P)
def lp(v):
    return loop(v)


@profile(precision=P)
def test_sieve():
    if len(sys.argv) == 1:
        n = 100000
    else:
        n = int(sys.argv[1])
    # t1 = se_e(n)
    # t2 = se(n)
    t3 = bf(n)


@profile(precision=P)
def test_l2_2():
    if len(sys.argv) == 1:
        size = 100
    else:
        size = int(sys.argv[1])
    value = int(''.join([str(random.randint(0, 10)) for i in range(size)]))
    print(value)
    # r = recur(value)
    l = lp(value)


def main():
    test_sieve()
    # test_l2_2()


if __name__ == '__main__':
    main()


'''
METHOD: test_sieve()
INPUT
N = 1000
OUTPUT
Line #    Mem usage    Increment   Line Contents
================================================
    51  16.38281 MiB   0.01953 MiB       t1 = se_e(n)
    52                                 # t2 = se(n)
    53                                 # t3 = bf(n)
    
    51                                 # t1 = se_e(n)
    52  16.41797 MiB   0.01953 MiB       t2 = se(n)
    53                                 # t3 = bf(n)

    51                                 # t1 = se_e(n)
    52                                 # t2 = se(n)
    53  16.39062 MiB   0.01953 MiB       t3 = bf(n)
    
    (значения у функций "Решето Эратосфена" скакало вверх, у функции перебора скачков не было)
------------------------------------------------
INPUT
N = 100000
OUTPUT
Line #    Mem usage    Increment   Line Contents
================================================
    51  19.51953 MiB   3.12109 MiB       t1 = se_e(n)
    52                                 # t2 = se(n)
    53                                 # t3 = bf(n)
    
    51                                 # t1 = se_e(n)
    52  19.56250 MiB   3.12500 MiB       t2 = se(n)
    53                                 # t3 = bf(n)

    51                                 # t1 = se_e(n)
    52                                 # t2 = se(n)
    53  20.32031 MiB   3.92188 MiB       t3 = bf(n)
******************************************************************************

METHOD: test_l2_2()
INPUT
size = 15
OUTPUT
Line #    Mem usage    Increment   Line Contents
================================================
    61  16.37500 MiB   0.02344 MiB       r = recur(value)
    62                                 # l = lp(value)
    
    61                                 # r = recur(value)
    62  16.39844 MiB   0.02344 MiB       l = lp(value)
------------------------------------------------
INPUT
size = 100
OUTPUT
Line #    Mem usage    Increment   Line Contents
================================================
    61  16.47656 MiB   0.09766 MiB       r = recur(value)
    62                                 # l = lp(value)
    
    61                                 # r = recur(value)
    62  16.44922 MiB   0.02344 MiB       l = lp(value)
******************************************************************************

ВЫВОДЫ
для алгоритмов поиска простых чисел: 
- функция перебора начинает уступать функциям "Решето Эратосфена" в использовании памяти при увеличении числа N

для алгоритмов подсчета четных и нечетных цифр:
- вариант функции через цикл болле эффективен, чем вариант через рекурсию

'''