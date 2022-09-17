class Must_read:
    try:
        with open('data.csv', 'r') as file:
            print(file.read())
    except FileNotFoundError as e:
        print(e)