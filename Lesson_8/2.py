"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib


def get_hash_sub_str(s):

    def get_hash(e):
        return hashlib.sha1(e.encode('utf-8')).hexdigest()

    r = []
    n = len(s)

    for i in range(n):
        for j in range(n, i, -1):
            sub_str = s[i:j]
            if sub_str in [s, ' ', '']:
                continue
            h = get_hash(sub_str)
            if h in r:
                break
            print(sub_str)
            r.append(h)
    return r


def main():
    text = input('Enter text')
    print('Substrings:')
    t = get_hash_sub_str(text)
    print('-' * 50)
    print('Substrings hashes:')
    print('\n'.join(t))
    print('-'*50)
    print(f'In {text} {len(t)} substring')


if __name__ == '__main__':
    main()
