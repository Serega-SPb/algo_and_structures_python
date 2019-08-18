"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

import sys
from pympler import asizeof


class Vector:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'( {self.start}; {self.end} )'

    def _get_legs(self):
        k1 = abs(self.start[0] - self.end[0])
        k2 = abs(self.start[1] - self.end[1])
        return k1, k2

    def get_length(self):
        k1, k2 = self._get_legs()
        return (k1 ** 2 + k2 ** 2) ** (1 / 2)

    def get_point(self):
        return self.end[0] - self.start[0], self.end[1] - self.start[1]

    def get_matrix(self):
        return [[self.start[0], self.end[0]], [self.start[1], self.end[1]]]


class VectorSlots:
    __slots__ = ('start', 'end')

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'( {self.start}; {self.end} )'

    def _get_legs(self):
        k1 = abs(self.start[0] - self.end[0])
        k2 = abs(self.start[1] - self.end[1])
        return k1, k2

    def get_length(self):
        k1, k2 = self._get_legs()
        return (k1 ** 2 + k2 ** 2) ** (1 / 2)

    def get_point(self):
        return self.end[0] - self.start[0], self.end[1] - self.start[1]

    def get_matrix(self):
        return [[self.start[0], self.end[0]], [self.start[1], self.end[1]]]


def main():
    p1 = (1, 5)
    p2 = (50, 10)

    v1 = Vector(p1, p2)
    v2 = VectorSlots(p1, p2)

    if hasattr(v1, '__dict__'):
        print(f'v1.__dict__: {v1.__dict__}')

    if hasattr(v2, '__dict__'):
        print(f'v2.__dict__: {v2.__dict__}')

    print('Vector size:')
    print(f'Pympler |  {asizeof.asizeof(v1)}')
    print(f'Sys     |  {sys.getsizeof(v1)}')

    print('VectorSlots size:')
    print(f'Pympler |  {asizeof.asizeof(v2)}')
    print(f'Sys     |  {sys.getsizeof(v2)}')


if __name__ == '__main__':
    main()
