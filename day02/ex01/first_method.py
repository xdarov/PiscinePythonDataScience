class Research:
    def file_reader(self):
        with open('data.csv', 'r') as file:
            return file.read()

def main():
    obj = Research()
    try:
        print(obj.file_reader())
    except OSError as e:
        print(e)

if __name__ == '__main__':
    main()