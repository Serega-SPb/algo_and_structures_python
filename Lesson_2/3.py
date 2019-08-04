"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def recursion():
    def shift(v, i=1, r=0):

        temp = v % (10 ** i) // (10 ** (i - 1))

        r *= 10
        r += temp

        if v // (10 ** i) == 0:
            return r
        return shift(v, i + 1, r)

    value = int(input('Введите чилос: '))
    result = shift(value)
    print(f' {value} -> {result}')


def loop():
    value_str = input('Введите чилос: ')
    value = int(value_str)
    result = i = j = r = 0
    while True:
        i += 1
        if value // (10 ** i) == 0:
            break
    i -= 1

    while i >= 0:
        value -= r
        temp = value // (10 ** i)

        r = temp * (10 ** i)
        result += temp * (10 ** j)

        i -= 1
        j += 1

    print(f' {value_str} -> {result}')


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
