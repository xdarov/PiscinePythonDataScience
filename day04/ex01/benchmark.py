#!python3
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
    

def main():
    n = 10000000
    loop_time = timeit.timeit('loop_list()', 'from __main__ import loop_list', number=n)

    compr_time = timeit.timeit('compr_list()', 'from __main__ import compr_list', number=n)

    map_time = timeit.timeit('map_list()', 'from __main__ import map_list', number=n)

    if loop_time > compr_time and map_time > compr_time:
        print('it is better to use a list comprehension')
    elif loop_time > map_time and compr_time > map_time:
        print('it is better to use a map')
    else:
        print('it is better to use a loop')
    
    print(*sorted([loop_time, compr_time, map_time]), sep=' vs ')

    # print(loop_list(), compr_list(), map_list(), sep='\n')

if __name__ == "__main__":
    main()