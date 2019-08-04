"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def print_answer(n, n_sum):
    print(f'n = {n} 1+2+...+n = {n_sum}')
    if n_sum == n*(n+1)/2:
        print('1+2+...+n = n(n+1)/2')
    else:
        print('1+2+...+n != n(n+1)/2')


def recursion():

    def get_sum(i=0, s=0):
        s += i
        if i == n:
            return s
        return get_sum(i+1, s)

    n = int(input('Введите N '))
    n_sum = get_sum()
    print_answer(n, n_sum)


def loop():

    n = int(input('Введите N '))
    n_sum = 0

    for i in range(1, n+1):
        n_sum += i

    print_answer(n, n_sum)


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
