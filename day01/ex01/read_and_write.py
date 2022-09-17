def read_file():
    with open('ds.csv', 'r') as file:
        data = file.read().split('\n')
        while '' in data:
            data.remove('')
    for i, elem in enumerate(data):
        elem = elem.split('"')
        mixin = '\t'.join(elem[6][1:-1].split(','))
        elem.pop(6)
        elem.insert(6, mixin)
        while '' in elem or ',' in elem:
            if '' in elem:
                elem.remove('')
            if ',' in elem:
                elem.remove(',')
        elem = '\t'.join(elem)
        data[i] = elem
    return '\n'.join(data)


if __name__ == "__main__":
    try:
        data = read_file()
        with open('ds.tsv', 'w') as file:
            file.write(data)
    except (PermissionError, FileNotFoundError) as e:
        print('ERROR: ', e)
