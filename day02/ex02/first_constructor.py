class Must_read:
    def __init__(self, file_name) -> None:
        self.file_name = file_name

    def file_reader(self):
        with open(self.file_name, 'r') as file:
            print(file.read())
        
if __name__ == '__main__':
    obj = Must_read()
    try:
        obj.file_reader()
    except FileNotFoundError as e:
        print(e)