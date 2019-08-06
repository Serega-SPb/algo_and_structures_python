# 4.	Определить, какое число в массиве встречается чаще всего.

from Lesson_3.array_functions import *


array = get_random_array(10, 1, 5)
checked = []
max_count = 0
result_value = 0

for i, n in get_enumerator(array):
    if n in checked:
        continue
    count = 0
    for j in array[i:]:
        if j == n:
            count += 1

    checked.append(n)
    if max_count < count:
        max_count = count
        result_value = n

print(f'Исходный массив:\n{output_format(array)}')
print(f'Результат: {result_value} Кол-во повторений: {max_count}')
