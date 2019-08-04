"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def recursion():
    def calc_sum(n, r=0, i=0):
        if n == 0:
            return r
        r += 1 / (2 ** i) * (1 if i % 2 == 0 else -1)
        return calc_sum(n-1, r, i+1)

    num = int(input('Введите N: '))
    result = calc_sum(num)
    print(result)


def loop():

    n = int(input('Введите N: '))
    result = 0

    # i = 0
    # while n > 0:
    #     result += 1 / (2 ** i) * (1 if i % 2 == 0 else -1)
    #     i += 1
    #     n -= 1

    for i in range(n):
        result += 1 / (2 ** i) * (1 if i % 2 == 0 else -1)
    print(result)


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
