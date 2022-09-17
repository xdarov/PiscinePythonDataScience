class Must_read:
    def file_reader(self):
        with open('data.csv', 'r') as file:
            print(file.read())
        
if __name__ == '__main__':
    obj = Must_read()
    try:
        obj.file_reader()
    except FileNotFoundError as e:
        print(e)