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

    def file_reader(self, has_header = True):
        try:
            with open(self.file_name, 'r') as file:
                data = file.read()
            self.check_struct(data)
            data = data.split('\n')
            if has_header:
                return [[int(i[0]),int(i[1])] for elem in data[1:] if (i := elem.split(','))]
            else:
                return [[int(i[0]),int(i[1])] for elem in data if (i := elem.split(','))]
        except (OSError, ValueError) as e:
            print('Exception: ', e)
    
    class Calculations:

        @classmethod
        def counts(cls, data: list):
            heads = 0
            tails = 0
            for i in data:
                if i[0] == 1:
                    heads += 1
                else:
                    tails += 1
            return heads, tails

        @classmethod
        def fractions(cls, head, tails):
            count = head + tails
            return  head / count * 100, tails / count * 100
            

def main():
    obj = Must_read(sys.argv[1])
    data = obj.file_reader()
    if data != None:
        print(data)
        counts = obj.Calculations.counts(data)
        print(*counts)
        print(*obj.Calculations.fractions(*counts))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()