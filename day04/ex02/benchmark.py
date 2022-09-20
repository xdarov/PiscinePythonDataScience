#!python3
import sys
import timeit

def get_mail_list():
    return ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

def loop_list(mail_list: list = get_mail_list()):
    result = []
    for i in mail_list:
        if i.find('@gmail.com') >= 0:
            result.append(i)
    return result
    
def compr_list(mail_list: list = get_mail_list()):
    return [i for i in mail_list if i.find('@gmail.com') >= 0]

def map_list(mail_list: list = get_mail_list()):
    result = []
    def func(x):
        if x.find('@gmail.com') >= 0:
            result.append(x)
    list(map(func, mail_list))
    return result

def filter_list(mail_list: list = get_mail_list()):
    result = []
    def func(x):
        if x.find('@gmail.com') >= 0:
            return x
    return list(filter(func, mail_list))
    

def main():
    
    func_dict = {'list_comprehension': 'compr_list',
                 'loop': 'loop_list',
                 'map': 'map_list',
                 'filter': 'filter_list'}
    
    if len(sys.argv) == 3 and sys.argv[1] in func_dict and sys.argv[2].isdigit():
        time = timeit.timeit(f'{func_dict[sys.argv[1]]}()',
                                f'from __main__ import {func_dict[sys.argv[1]]}',
                                number=int(sys.argv[2]))
        print(time)
    else:
        print('Bad Arg')

    # print(loop_list(), compr_list(), map_list(), filter_list(), sep='\n')

if __name__ == "__main__":
    main()