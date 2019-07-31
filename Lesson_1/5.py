# 5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

import sys

num_a = ord('a')
num_z = ord('z')

char_first = input('Введите первую букву: ')
char_second = input('Введите вторую букву: ')

if char_first == char_second:
    print('Символы одинаковые')
    sys.exit()

try:
    num_first = ord(char_first)
    num_second = ord(char_second)
except TypeError:
    print('Некорректный ввод')
    sys.exit()

if not num_a <= num_first <= num_z or not num_a <= num_second <= num_z:
    print('Символы не строчные буквы английского алфавита')
    sys.exit()

pos_first = num_first - num_a + 1
pos_second = num_second - num_a + 1

if pos_first > pos_second:
    dist = pos_first - pos_second
else:
    dist = pos_second - pos_first

print(f'Позиция 1-й буквы:\n- в английском алфавите {pos_first}\n- в таблице символов {num_first}')
print(f'Позиция 2-й буквы:\n- в английском алфавите {pos_second}\n- в таблице символов {num_second}')
print(f'{dist} букв между {char_first} и {char_second}')
