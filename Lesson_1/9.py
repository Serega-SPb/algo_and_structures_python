# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

import sys

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))


if first == second or second == third or third == first:
    print('2 числа одинаковые')
    sys.exit()

if first > second:
    if first > third:
        max_value = first

        if second > third:
            mid_value = second
            min_value = third
        else:
            mid_value = third
            min_value = second
    else:
        max_value = third
        mid_value = first
        min_value = second
else:
    if second > third:
        max_value = second

        if first > third:
            mid_value = first
            min_value = third
        else:
            mid_value = third
            min_value = first
    else:
        max_value = third
        mid_value = second
        min_value = first

print(f'MAX: {max_value}\nMID: {mid_value}\nMIN: {min_value}')
print(f'{min_value} < {mid_value} < {max_value}')

