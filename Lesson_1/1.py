# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

import sys

number = int(input('Введите трехзначное число:'))

first = number // 100

if first == 0 or first > 9:
    print('Число не трехзначное')
    sys.exit()

second = (number - first * 100) // 10
third = number - first * 100 - second * 10

result_sum = first + second + third
result_mult = first * second * third

print(f'{first} + {second} + {third} = {result_sum}')
print(f'{first} * {second} * {third} = {result_mult}')
