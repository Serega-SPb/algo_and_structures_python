from multiprocessing import cpu_count
from multiprocessing.dummy import Pool


def bubble_sort(array, asc=True):
    n = len(array) - 1

    for i in range(n-1):
        break_flag = True
        for j in range(n-i):

            cond = array[j] > array[j + 1] if asc else array[j] < array[j + 1]
            if cond:
                array[j], array[j+1] = array[j+1], array[j]
                break_flag = False
        if break_flag:
            break
    return array


def merge_sort(array, asc=True):
    size = len(array)
    if size <= 1:
        return array

    c = size // 2
    left = array[:c]
    right = array[c:]

    left = merge_sort(left, asc)
    right = merge_sort(right, asc)

    lt = rt = 0
    result = []
    while lt < len(left) and rt < len(right):

        cond = left[lt] < right[rt] if asc else left[lt] > right[rt]
        if cond:
            result.append(left[lt])
            lt += 1
        else:
            result.append(right[rt])
            rt += 1

    if lt == len(left):
        result.extend(right[rt:])
    else:
        result.extend(left[lt:])

    return result


used_processes = 0
CPU_COUNT = cpu_count()


# попытка сделать multi threading
def merge_sort_parallel(array, asc=True):
    global used_processes
    size = len(array)
    if size <= 1:
        return array

    c = size // 2
    left = array[:c]
    right = array[c:]
    if used_processes < CPU_COUNT:
        used_processes += 2
        with Pool(2) as pool:
            left, right = pool.starmap(merge_sort_parallel, [(left, asc), (right, asc)])
    else:
        left = merge_sort(left, asc)
        right = merge_sort(right, asc)

    lt = rt = 0
    result = []
    while lt < len(left) and rt < len(right):

        cond = left[lt] < right[rt] if asc else left[lt] > right[rt]
        if cond:
            result.append(left[lt])
            lt += 1
        else:
            result.append(right[rt])
            rt += 1

    if lt == len(left):
        result.extend(right[rt:])
    else:
        result.extend(left[lt:])

    return result
