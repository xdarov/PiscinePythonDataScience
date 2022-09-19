class Must_read:
    try:
        with open('data.csv', 'r') as file:
            print(file.read())
    except OSError as e:
        print(e)