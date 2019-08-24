"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

from collections import Counter


class BinaryTree:

    __slots__ = ('value', 'parent', 'left_child', 'right_child')

    def __init__(self, value, **kwargs):
        self.value = value
        self.parent = kwargs.get('parent', None)
        self.left_child = kwargs.get('left', None)
        self.right_child = kwargs.get('right', None)

    def get_root(self):
        if self.parent:
            return self.parent.get_root()
        return self

    def add_child_left(self, value):
        b = BinaryTree(value, parent=self)
        self.left_child = b

    def add_child_right(self, value):
        b = BinaryTree(value, parent=self)
        self.right_child = b

    def get_table(self):
        table = {}
        paths = self.get_path()
        for i in range(0, len(paths)-1, 2):
            table[paths[i]] = paths[i+1]
        return table
        # return dict(sorted(table.items(), key=lambda kv: len(kv[1])))

    def get_path(self, code=''):
        result = []
        if self.value and self.value is not None:
            return self.value, code

        if self.left_child:
            result.extend(self.left_child.get_path(f'{code}0'))
        if self.right_child:
            result.extend(self.right_child.get_path(f'{code}1'))
        return result

    def print_tree(self):

        cell_size = 5
        message = ''

        def get_value(branch):
            return f"'{branch.value}'" if branch.value is not None else '   '

        center = cell_size * (len(max(self.get_path(), key=lambda x: len(x))) + 5)

        message += ' ' * (center + (cell_size // 2))
        message += f"({get_value(self)})"
        message += '\n'

        center -= int(cell_size * 1.5)
        left_cursor = center // 2 - (cell_size // 2 + 1)
        right_cursor = left_cursor + center * 2 - cell_size * 2
        children_queue = [(self.left_child, left_cursor, 'L'), (self.right_child, right_cursor, 'R')]

        for child, pos, flag in children_queue:
            if child.left_child is not None:
                children_queue.append((child.left_child, pos - cell_size + 1, 'L'))
            if child.right_child is not None:
                children_queue.append((child.right_child, pos + cell_size - 1, 'R'))

        last_pos = 0
        last_flag = ''
        while len(children_queue) > 0:

            cell, pos, flag = children_queue.pop(0)

            if last_pos > pos:
                last_pos = 0
                message += '\n'
            if last_flag == 'L' and flag == 'R':
                message += f'{"|":-^{(pos - last_pos)}}'
            else:
                message += ' ' * (pos - last_pos)
            message += f"({get_value(cell)})"

            last_pos = pos + cell_size
            last_flag = flag

        print(message)

    def __str__(self):

        s = f'{self.value} '

        if self.left_child or self.right_child:
            s += f': [ 0: {self.left_child} | 1: {self.right_child} ]'
        return s


def test_tree():
    tr = BinaryTree('ST')
    curr = tr
    while True:

        action = input('L| R | P | AL | AR | Q').upper()

        if action == 'Q':
            break

        if action in ['L', 'R', 'P']:
            if action == 'L' and curr.left_child:
                curr = curr.left_child
            if action == 'R' and curr.right_child:
                curr = curr.right_child
            if action == 'P' and curr.parent:
                curr = curr.parent
        else:
            value = input('VALUE')
            if action == 'AL':
                curr.add_child_left(value)
            if action == 'AR':
                curr.add_child_right(value)

        print(f'CURR - {curr}')

    print(tr)


def get_tree(text):

    priority = sorted(Counter(text).items(), key=lambda x: -x[1])
    branches = []

    for c, p in priority:
        b = BinaryTree(c)
        branches.append((p, b))
    del priority

    while len(branches) > 1:

        lt = branches.pop()
        rt = branches.pop()
        w = lt[0] + rt[0]
        b = BinaryTree(None, left=lt[1], right=rt[1])

        for i, p in enumerate(branches):
            if p[0] < w:
                branches.insert(i, (w, b))
                break
        else:
            branches.append((w, b))

    return branches.pop()[1]


def encoding_huffman(text):
    tree = get_tree(text)
    table = tree.get_table()
    encoded_text = ''
    for t in text:
        encoded_text += table[t]
    return tree, table, encoded_text


def decoding_huffman(table, encoded_text):
    rev_table = dict([(v, k) for k, v in table.items()])

    code = ''
    decoded_text = ''
    for c in encoded_text:
        code += c
        if code in rev_table:
            decoded_text += rev_table[code]
            code = ''
    return decoded_text


def binary_format(binary):
    formatted_binary = ''
    for i, b in enumerate(binary):
        formatted_binary += b
        if i != 0 and i % 4 == 0:
            formatted_binary += ' '
    return formatted_binary


def main():
    import random
    text = ''.join([random.choice('abcdef') for _ in range(25)])
    # text = 'bedbaaeaafdddea'
    # text = 'abracadabra'
    # text = 'beep boop beer!'
    print(f'INPUT:\n {text}')
    tree, table, encoded = encoding_huffman(text)
    print(f'ENCODED:\n {binary_format(encoded)}')
    decoded = decoding_huffman(table, encoded)
    print(f'DECODED:\n{decoded}')
    print('CODE TABLE')
    print(sorted(table.items(), key=lambda x: len(x[1])))
    print('Binary tree:')
    tree.print_tree()


if __name__ == '__main__':
    main()
