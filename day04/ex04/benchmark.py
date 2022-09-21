#!python3
import timeit
import random
from collections import Counter


def get_random_list():
    return [random.randint(0,100) for i in range(1000000)]

def get_dict(rand_list: list = get_random_list()):
    if not rand_list:
        return
    dict_count = {}
    for i in set(rand_list):
        dict_count[i] = rand_list.count(i)
    return dict_count

def top_numbers(dict_count: dict = get_dict()):
    if not dict_count:
        return
    list_tuple = sorted(dict_count.items(), key=lambda x: x[1], reverse=True)
    return [i[0] for i in list_tuple[:10]]

def get_dict_counter(rand_list: list = get_random_list()):
    if not rand_list:
        return
    return Counter(rand_list)

def top_numbers_counter(dict_count: Counter = get_dict_counter()):
    if not dict_count:
        return
    list_tuple = dict_count.most_common()
    return [i[0] for i in list_tuple[:10]]

def main():
    dict_time = timeit.timeit('get_dict()', 'from __main__ import get_dict', number=1)
    top_numbers_time = timeit.timeit('top_numbers()', 'from __main__ import top_numbers', number=1)
    dict_time_counter = timeit.timeit('get_dict_counter()', 'from __main__ import get_dict_counter', number=1)
    top_numbers_time_counter = timeit.timeit('top_numbers_counter()', 'from __main__ import top_numbers_counter', number=1)

    print(f"my function: {dict_time}\n" \
          f"Counter: {dict_time_counter}\n" \
          f"my top: {top_numbers_time}\n" \
          f"Counter's top:{top_numbers_time_counter}")

if __name__ == '__main__':
    main()