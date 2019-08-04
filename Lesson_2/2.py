"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


def recursion():

    def shift(v, i=1, o=0, e=0):

        temp = v % (10 ** i) // (10 ** (i-1))

        if temp % 2 == 0:
            e += 1
        else:
            o += 1

        if v // (10 ** i) == 0:
            return o, e
        return shift(v, i + 1, o, e)

    value = int(input('Введите чилос: '))
    odd_count, even_count = shift(value)
    print(f'В {value} \nчетных: {even_count} \nнечетных: {odd_count}')


def loop():

    value_str = input('Введите чилос: ')    # var to print
    value = int(value_str)
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

    print(f'В {value_str} \nчетных: {even_count} \nнечетных: {odd_count}')


def main():

    exit_flag = False
    while not exit_flag:
        mode = input('Recursion(R) or Loop(L) (0-exit)').upper()
        if mode == 'L':
            loop()
        elif mode == 'R':
            recursion()
        elif mode == '0':
            exit_flag = True


if __name__ == '__main__':
    main()
