from random import randint


class Research:
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

        def __init__(self, data: list):
            self.data: list = data

        def counts(self):
            heads = 0
            tails = 0
            for i in self.data:
                if i[0] == 1:
                    heads += 1
                else:
                    tails += 1
            return heads, tails

        @classmethod
        def fractions(cls, head, tails):
            count = head + tails
            return  head / count * 100, tails / count * 100
    

    class Analytics(Calculations):
        
        def predict_random(self, count):
            return [[1,0] if randint(0,1) > 0 else [0,1] for i in range(count)]

        def predict_last(self, Research):
            data = Research.file_reader()
            if len(data) > 0:
                return data[-1]
        
        def save_file(self, data, file_name, extension):
            with open(f"{file_name}.{extension}", 'w') as file:
                file.write(str(data))

