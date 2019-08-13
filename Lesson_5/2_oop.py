
from collections import deque


class Hex:

    def __init__(self, *args):
        self.value = deque(args)

    def __add__(self, other):
        temp = self.value_as_int() + other.value_as_int()
        return Hex(hex(temp)[2:])

    def __mul__(self, other):
        temp = self.value_as_int() * other.value_as_int()
        return Hex(hex(temp)[2:])

    def value_as_int(self):
        return int(''.join(self.value), 16)

    def __str__(self):
        return ''.join(self.value).upper()


def main():

    hex_lt = Hex(input('Введите 1-е шестнадцатеричное число: '))
    hex_rt = Hex(input('Введите 2-е шестнадцатеричное число: '))

    result_sum = hex_lt + hex_rt
    result_mul = hex_lt * hex_rt

    print(f'{hex_lt} + {hex_rt} = {result_sum}')
    print(f'{hex_lt} * {hex_rt} = {result_mul}')


if __name__ == '__main__':
    main()
