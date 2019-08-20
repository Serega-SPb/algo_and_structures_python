from timeit import timeit
import random


START = 0
END = 50


def main():

    size = int(input('Enter array size: '))
    count = int(input('Enter count: '))
    array = [round(random.uniform(START, END), 2) for _ in range(size)]

    print('Bubble sort')
    print(timeit(f'bubble_sort({array})', setup='from Lesson_7.sort_functions import bubble_sort', number=count))
    print('Merge sort')
    print(timeit(f'merge_sort({array})', setup='from Lesson_7.sort_functions import merge_sort', number=count))

    print('Merge sort parallel')
    print(timeit(f'merge_sort_parallel({array})', setup='from Lesson_7.sort_functions import merge_sort_parallel', number=count))


if __name__ == '__main__':
    main()

"""
-------------------------
Enter array size: 1000
Enter count: 10
Bubble sort
1.2573218000000002
Merge sort
0.05348160000000046
Merge sort parallel
0.4327228000000005

-------------------------

Enter array size: 10000
Enter count: 1
Bubble sort
13.481214399999999
Merge sort
0.07108270000000161
Merge sort parallel
0.3227706999999995

-------------------------

Enter array size: 1000
Enter count: 1000
Merge sort
5.2023164
Merge sort parallel
5.486009599999999

-------------------------
"""