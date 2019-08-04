"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def get_len(value):
    i = 0
    while True:
        i += 1
        if value // (10 ** i) == 0:
            break
    return i


def parse_num(num, num_len):
    r = 0
    while num_len >= 0:
        num -= r
        temp = num // (10 ** num_len)
        r = temp * (10 ** num_len)
        num_len -= 1
        yield temp


def recursion():

    def calc_sum(n, i=1, s=0):
        temp = n % (10 ** i) // (10 ** (i - 1))
        s += temp
        if n // (10 ** i) == 0:
            return s
        return calc_sum(n, i + 1, s)

    def get_num():

        nonlocal result
        nonlocal max_sum

        value = input('Введите число ("" - закончить ввод): ')
        if value is None or not value.isdigit():
            return
        num = int(value)
        num_sum = calc_sum(num)

        if max_sum < num_sum:
            max_sum = num_sum
            result = num

        get_num()

    result = 0
    max_sum = 0
    get_num()
    print(f'Результат: {result}, Сумма: {max_sum}')


def loop():

    result = 0
    max_sum = 0

    while True:

        value = input('Введите число ("" - закончить ввод): ')
        if value is None or not value.isdigit():
            break

        num = int(value)
        num_len = get_len(num)
        num_sum = 0

        for n in parse_num(num, num_len-1):
            num_sum += n

        if max_sum < num_sum:
            max_sum = num_sum
            result = num

    print(f'Результат: {result}, Сумма: {max_sum}')


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
