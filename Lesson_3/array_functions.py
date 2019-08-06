import random


def get_random(min_value, max_value):
    return random.random() * (max_value - min_value) + min_value


def get_random_array(size, start, end):
    array = []

    if start > end:
        start, end = end, start

    for i in range(size):
        array.append(int(get_random(start, end)))
    return array


def get_array(start, end):
    array = []

    if start > end:
        start, end = end, start
    size = end - start

    for i in range(size):
        array.append(start+i)
    return array


def get_enumerator(array, i=0):
    for j in array:
        yield i, j
        i += 1


# output_format = lambda x: [f'{y:>3}' for y in x]
def output_format(array, s=3):
    return ' '.join([f'{i:>{s}}' for i in array])


def get_sorted(array):
    result = []
    for i in array:
        if result is None:
            result.append(i)
            continue
        ins_pos = 0
        for j, n in get_enumerator(result):
            if i > n:
                ins_pos = j+1
            else:
                break
        result.insert(ins_pos, i)
    return result
