# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

point_a_x = float(input('Введите координату X точки A: '))
point_a_y = float(input('Введите координату Y точки A: '))
point_b_x = float(input('Введите координату X точки B: '))
point_b_y = float(input('Введите координату Y точки B: '))


k = (point_a_y - point_b_y) / (point_a_x - point_b_x)
b = point_a_y - k * point_a_x

print(f'{point_a_y:.2f} = {k:.2f}* {point_a_x:.2f} + {b:.2f}')
print(f'{point_b_y:.2f} = {k:.2f}* {point_b_x:.2f} + {b:.2f}')
