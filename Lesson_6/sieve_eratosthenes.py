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
    del a
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


def main():

    n = int(input('Enter N: '))
    print('Select method')
    print('brute_force - B, sieve_eratosthenes - E, sieve_eratosthenes_exm - EX')
    m = input('Method: ').upper()

    if m == 'E':
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
