"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

import random

TRY_COUNT = 10


def get_random(min_value, max_value):
    return random.random() * (max_value - min_value) + min_value


def recursion():

    def game(i=0):

        answer = int(input(f'Угадайте число от 0 до 100 (осталось попыток: {TRY_COUNT - i}): '))

        if answer == quest:
            print('Поздравляю, вы угадали!')
            return
        elif answer > quest:
            print('Вы ввели слишком большое число')
        elif answer < quest:
            print('Вы ввели слишком маленькое число')

        i += 1
        if i < TRY_COUNT:
            game(i)
        else:
            print(f'GAME OVER\nПравильный ответ: {quest}')

    quest = int(get_random(0, 100))
    game()


def loop():

    quest = int(get_random(0, 100))

    for i in range(TRY_COUNT):
        answer = int(input(f'Угадайте число от 0 до 100 (осталось попыток: {TRY_COUNT - i}): '))

        if answer == quest:
            print('Поздравляю, вы угадали!')
            break
        elif answer > quest:
            print('Вы ввели слишком большое число')
        elif answer < quest:
            print('Вы ввели слишком маленькое число')
    else:
        print(f'GAME OVER\nПравильный ответ: {quest}')


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
