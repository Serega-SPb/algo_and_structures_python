import sys
import os


def main():

    exit_flag = False

    tasks = list(range(1, 10))

    while not exit_flag:

        task = int(input(f'Enter task number(1-{len(tasks)}) 0-exit: '))

        if task == 0:
            sys.exit()

        if task in tasks:
            os.system(f'python {task}.py')


if __name__ == '__main__':
    main()