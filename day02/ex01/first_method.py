class Research:
    def file_reader(self):
        with open('data.csv', 'r') as file:
            print(file.read())
        
if __name__ == '__main__':
    obj = Research()
    try:
        obj.file_reader()
    except FileNotFoundError as e:
        print(e)