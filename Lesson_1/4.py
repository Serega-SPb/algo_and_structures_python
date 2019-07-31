"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

import random


def get_random(min_value, max_value):
    return random.random() * (max_value - min_value) + min_value


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


threshold_start = input('Введите начало диапазона: ')
threshold_end = input('Введите конец диапазона: ')

if threshold_start < threshold_end:
    start = threshold_start
    end = threshold_end
else:
    start = threshold_end
    end = threshold_start

if start.isdigit() and end.isdigit():
    result = int(get_random(int(start), int(end)+1))
elif isfloat(start) and isfloat(end):
    result = round(get_random(float(start), float(end)+0.01), 2)
else:
    start = ord(start)
    end = ord(end)+1
    result = chr(int(get_random(start, end)))

print(f'Результат: {result}')
