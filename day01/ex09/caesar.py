import sys

def encode(shift: int):
    result = ''
    shift = shift % 26
    print(sys.argv[2])
    for i in sys.argv[2]:
        if ord(i) > 126:
            raise ValueError('The script does not support your language yet')
        if i.isupper() and i.isalpha():
            result += chr(ord(i) + shift if ord(i) + shift < 91 else 65 + ord(i) + shift - 91)
        elif i.islower() and i.isalpha():
            result += chr(ord(i) + shift if ord(i) + shift < 123 else 97 + ord(i) + shift - 123)
        else:
            result += i
        # print(i, result[-1])
    return result

def decode(shift: int):
    result = ''
    shift = shift % 26
    for i in sys.argv[2]:
        if ord(i) > 126:
            raise ValueError('The script does not support your language yet')
        if i.isupper() and i.isalpha():
            result += chr(ord(i) - shift if ord(i) - shift > 64 else 91 - (65 - (ord(i) - shift)))
        elif i.islower() and i.isalpha():
            result += chr(ord(i) - shift if ord(i) - shift > 96 else 123 - (97 - (ord(i) - shift)))
        else:
            result += i
    return result

if __name__ == '__main__':
    try:
        if len(sys.argv) == 4:
            if sys.argv[3].isdigit():
                shift = int(sys.argv[3])
            else:
                raise ValueError('shift not a num')
            if sys.argv[1] == 'encode':
                print(encode(shift))
            elif sys.argv[1] == 'decode':
                print(decode(shift))
            else:
                raise ValueError('Bad Arg')
        else:
            raise ValueError('Count of arg')
    except ValueError as e:
        print('Exception:', e)




