# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

from Lesson_3.array_functions import *


array = get_array(2, 100)
m_array = get_array(2, 10)
result = []

for j in m_array:
    result.append(0)

for i in array:
    for j, m in get_enumerator(m_array):
        if i % m == 0:
            result[j] += 1

print(f'Диапазон             {output_format(m_array)}')
print(f'Кол-во кратных чисел {output_format(result)}')
