def data_types():
    type_list = [type(10).__name__,
                 type('string').__name__,
                 type(2.5).__name__,
                 type(True).__name__,
                 type(['one', 'two', 'three']).__name__,
                 type({'one':1}).__name__,
                 type((1, 2, 'three')).__name__,
                 type({'one', 'two', 3}).__name__,
                ]
    print(str(type_list).replace("'", ""))


if __name__ == '__main__':
    data_types()
