import sys

def to_dictionary():
    list_of_tuples = [
                ('Russia', '25'),
                ('France', '132'),
                ('Germany', '132'),
                ('Spain', '178'),
                ('Italy', '162'),
                ('Portugal', '17'),
                ('Finland', '3'),
                ('Hungary', '2'),
                ('The Netherlands', '28'),
                ('The USA', '610'),
                ('The United Kingdom', '95'),
                ('China', '83'),
                ('Iran', '76'),
                ('Turkey', '65'),
                ('Belgium', '34'),
                ('Canada', '28'),
                ('Switzerland', '26'),
                ('Brazil', '25'),
                ('Austria', '14'),
                ('Israel', '12')
                ]
    rare_dict = {}

    for elem in list_of_tuples:
        rare_dict[f"'{elem[1]}' : '{elem[0]}'"] = ''
    for elem in rare_dict.keys():
        print(elem)
    

if __name__ == '__main__':
    if len(sys.argv) == 1:
        to_dictionary()