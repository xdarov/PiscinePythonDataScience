def dict_sorter():
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
        rare_dict[elem[0]] = elem[1]
    
    rare_list = []

    for elem in rare_dict.items():
        rare_list.append(elem)
    rare_list = sorted(rare_list)
    rare_list = sorted(rare_list, reverse=True, key=lambda typ: int(typ[1]))
    for elem in rare_list:
        print(elem[0], elem[1]) 

if __name__ == '__main__':
    dict_sorter()