#!python3
import sys
import timeit
from functools import reduce

def get_n():
    if len(sys.argv) == 4 and sys.argv[3].isdigit():
        return int(sys.argv[3])

def loop_sqrt_sum(n: int = get_n()):
    if not n:
        return
    result = 0
    for i in range(1, n + 1):
        result += i * i
    return result

def reduce_sqrt_sum(n: int = get_n()):
    if not n:
        return
    def func(x, y):
        return x + y * y
    return reduce(func, range(1, n + 1))


def main():
    func_dict = {'loop': 'loop_sqrt_sum',
                 'reduce': 'reduce_sqrt_sum'}

    if sys.argv[1] in func_dict and sys.argv[2].isdigit() and sys.argv[3].isdigit():
        time = timeit.timeit(f'{func_dict[sys.argv[1]]}()',
                                f'from __main__ import {func_dict[sys.argv[1]]}',
                                number=int(sys.argv[2]))
        print(time)
    else:
        print('Bad Arg')

if __name__ == "__main__":
    if len(sys.argv) == 4:
        main()