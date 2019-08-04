"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
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

    def counter(n, i=1, s=0):
        temp = n % (10 ** i) // (10 ** (i - 1))
        if target == temp:
            s += 1
        if n // (10 ** i) == 0:
            return s
        return counter(n, i+1, s)

    def get_num(j=0, r=0):
        if j < num_count:
            r += counter(int(input('Введите число: ')))
            r = get_num(j+1, r)
        return r

    target = int(input('Введите цифру для поиска: '))
    num_count = int(input('Введите кол-во чисел: '))
    result = get_num()
    print(f'Цифра {target} встретилась {result} раз')


def loop():

    target = int(input('Введите цифру для поиска: '))
    num_count = int(input('Введите кол-во чисел: '))
    result = 0

    for i in range(num_count):

        num = int(input('Введите число: '))
        num_len = get_len(num)

        for j in parse_num(num, num_len-1):
            if j == target:
                result += 1

    print(f'Цифра {target} встретилась {result} раз')


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
