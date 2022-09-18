import sys


class Must_read:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def check_struct(self, data: str) -> bool:
        data = data.split('\n')
        for i, value in enumerate(data):
            value = value.strip().split(',')
            if len(value) != 2:
                raise ValueError('Bad Struct of file')
            elif i > 0 and ('0' not in value or '1' not in value):
                raise ValueError('Bad Struct of file')

    def file_reader(self):
        try:
            with open(self.file_name, 'r') as file:
                data = file.read()
            self.check_struct(data)
            return data
        except (OSError, ValueError) as e:
            print('Exception: ', e)


def main():
    obj = Must_read(sys.argv[1])
    data = obj.file_reader()
    if data != None:
        print(data)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()