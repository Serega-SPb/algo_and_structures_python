"""
Посчитать четные и нечетные цифры введенного натурального числа.
"""


def recursion(value):

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


def loop(value):

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
