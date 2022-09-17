import sys

def let_start(f):
    res = ''
    with open(f, 'r') as filename:
        for line in filename:
            if line.__contains__('@'):
                email = line.strip().split('@')[0]
                name = email.split('.')[0].capitalize()
                surname = email.split('.')[1].capitalize()
                res = res + name + '\t' + surname + '\t' + line
    save_file (res )

def save_file(res):
    filename = 'employees.tsv'
    with open(filename, 'w') as f:
        f.write(res)

if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            let_start(sys.argv[1])
        else:
            raise ValueError('Count of arg')
    except ValueError as e:
        print('Exception:', e)
