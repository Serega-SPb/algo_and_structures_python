"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

HEX = '0123456789ABCDEF'


def hex_add(hex_lt, hex_rt):
    result = deque()

    len_lt = len(hex_lt)
    len_rt = len(hex_rt)

    if len_lt > len_rt:
        first = hex_lt
        second = hex_rt
        min_len = len_rt
    else:
        first = hex_rt
        second = hex_lt
        min_len = len_lt

    first.reverse()
    second.reverse()

    over = 0
    for i, c in enumerate(first):

        if i >= min_len:
            index_sum = HEX.index(c)
        else:
            index_sum = HEX.index(c) + HEX.index(second[i])

        if over != 0:
            index_sum += over
            over = 0

        if index_sum >= 16:
            res = index_sum % 16
            over += index_sum // 16
            result.append(HEX[res])
        else:
            result.append(HEX[index_sum])

    if over != 0:
        result.append(HEX[over])

    result.reverse()
    return result


def hex_mul(hex_lt, hex_rt):
    result = deque()

    hex_lt.reverse()
    hex_rt.reverse()

    temp_elems = []

    for i in hex_lt:
        temp_elem = deque()
        over = 0
        for j in hex_rt:
            index_mult = HEX.index(i) * HEX.index(j)

            if over != 0:
                index_mult += over
                over = 0

            if index_mult >= 16:
                res = index_mult % 16
                over += index_mult // 16
                temp_elem.append(HEX[res])
            else:
                temp_elem.append(HEX[index_mult])
        if over != 0:
            temp_elem.append(HEX[over])
        temp_elems.append(temp_elem)

    for i in range(len(temp_elems)):
        if i == 0:
            result = temp_elems[i]
            result.reverse()
            continue
        rt = temp_elems[i]
        rt.reverse()
        rt.extend(['0']*i)
        result = hex_add(result, rt)

    return result


def main():

    hex_lt = deque(input('Введите 1-е шестнадцатеричное число: ').upper())
    hex_rt = deque(input('Введите 2-е шестнадцатеричное число: ').upper())

    result_sum = hex_add(hex_lt.copy(), hex_rt.copy())
    result_mul = hex_mul(hex_lt.copy(), hex_rt.copy())

    print(f'{"".join(hex_lt)} + {"".join(hex_rt)} = {"".join(result_sum)}')
    print(f'{"".join(hex_lt)} * {"".join(hex_rt)} = {"".join(result_mul)}')


if __name__ == '__main__':
    main()
