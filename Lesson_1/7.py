"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

len_first = float(input('Введите длину 1-го отрезка: '))
len_second = float(input('Введите длину 2-го отрезка: '))
len_third = float(input('Введите длину 3-го отрезка: '))

check_1 = len_first < len_second + len_third
check_2 = len_second < len_second + len_first
check_3 = len_third < len_first + len_second

if check_1 and check_2 and check_3:
    if len_first == len_second:
        if len_first == len_third:
            state = 'равносторонним'
        else:
            state = 'равнобедренным'
    elif len_first == len_third:
        state = 'равнобедренным'
    else:
        if len_second == len_third:
            state = 'равнобедренным'
        else:
            state = 'разносторонним'
    print(f'Треугольник является {state}')
else:
    print('Треугольник не может существовать')


