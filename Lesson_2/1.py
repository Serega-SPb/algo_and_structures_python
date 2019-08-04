"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


def recursion():

    operation = input('Введите операцию ( "+" | "-" | "*" | "/" ) 0-выход')

    if operation == '0':
        return

    first_value = int(input('Введите первое число'))
    second_value = int(input('Введите второе число'))

    if operation == '+':
        print(f'Результат: {first_value + second_value}')
    elif operation == '-':
        print(f'Результат: {first_value - second_value}')
    elif operation == '*':
        print(f'Результат: {first_value * second_value}')
    elif operation == '/':
        if second_value == 0:
            print('Ошибка: деление на 0')
        else:
            print(f'Результат: {first_value / second_value}')
    else:
        print('Ошибка: неизвестная операция')
    recursion()


def loop():

    while True:
        operation = input('Введите операцию ( "+" | "-" | "*" | "/" ) 0-выход')

        if operation == '0':
            break

        first_value = int(input('Введите первое число'))
        second_value = int(input('Введите второе число'))

        if operation == '+':
            print(f'Результат: {first_value + second_value}')
        elif operation == '-':
            print(f'Результат: {first_value - second_value}')
        elif operation == '*':
            print(f'Результат: {first_value * second_value}')
        elif operation == '/':
            if second_value == 0:
                print('Ошибка: деление на 0')
            else:
                print(f'Результат: {first_value / second_value}')
        else:
            print('Ошибка: неизвестная операция')


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
