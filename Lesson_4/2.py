"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

from timeit import timeit


def sieve_eratosthenes_exm(n):
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b


def sieve_eratosthenes(n):

    a = list(range(n))
    a[1] = 0

    for m in a[2:]:
        if a[m] == 0:
            continue

        for j in range(m*2, n, m):
            a[j] = 0

    r = []
    for i in a:
        if i == 0:
            continue
        r.append(i)
    return r


def brute_force(n):

    num_array = list(range(2, n))
    result = []

    for i in num_array:
        if i in result:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)
    return result


def time_test(n):

    count = int(input('Number: '))
    methods = ['brute_force', 'sieve_eratosthenes_exm', 'sieve_eratosthenes']
    cl = len(max(methods))
    for m in methods:
        time = timeit(f'{m}({n})', setup=f'from __main__ import {m}', number=count)
        print(f'{m.capitalize():<{cl}}: {time}')


def main():

    n = int(input('Enter N: '))
    print('Select method')
    print('Test time - T, brute_force - B, sieve_eratosthenes - E, sieve_eratosthenes_exm - EX')
    m = input('Method: ').upper()

    if m == 'T':
        time_test(n)
        return
    elif m == 'E':
        result = sieve_eratosthenes(n)
    elif m == 'EX':
        result = sieve_eratosthenes_exm(n)
    elif m == 'B':
        result = brute_force(n)
    else:
        return

    print(result)


if __name__ == '__main__':
    main()
    pass


'''
Сложность:
brute_force - O(n^2)
sieve_eratosthenes - O(n*log(log n))
sieve_eratosthenes_exm - O(n*log(log n))


Method: Test time
---------------------------------------------------
INPUT:
Enter N: 10      Number: 500
OUTPUT:
Brute_force           : 0.006414900000000223
Sieve_eratosthenes_exm: 0.009184399999999648
Sieve_eratosthenes    : 0.00630430000000004
---------------------------------------------------
INPUT:
Enter N: 100     Number: 500
OUTPUT:
Brute_force           : 0.14554310000000026
Sieve_eratosthenes_exm: 0.07847960000000054
Sieve_eratosthenes    : 0.047155499999999684
---------------------------------------------------
INPUT:
Enter N: 1000    Number: 500
OUTPUT:
Brute_force           : 8.810421000000002
Sieve_eratosthenes_exm: 0.9454638000000024
Sieve_eratosthenes    : 0.5375639999999997
---------------------------------------------------
'''