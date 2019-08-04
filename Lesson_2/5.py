"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

START = 32
END = 127


def get_num_char(num):
    return f'{num:<3} {chr(num)}'


def recursion():

    def get_separator():
        nonlocal counter
        counter += 1
        if counter == 10:
            counter = 0
            return '\n'
        return '  '

    def message_format(m=''):
        nonlocal current
        m += get_num_char(current)
        m += get_separator()
        if current == END:
            return m
        current += 1
        return message_format(m)

    current = START
    counter = 0
    print('-' * 75)
    print(message_format())
    print('-' * 75)


def loop():

    c = 1
    message = ''
    for i in range(START, END + 1):
        message += get_num_char(i)

        sep = '  '
        if c == 10:
            sep = '\n'
            c = 0
        message += sep
        c += 1

    print('-' * 75)
    print(message)
    print('-' * 75)


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
