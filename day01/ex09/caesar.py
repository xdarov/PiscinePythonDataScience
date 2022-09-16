from curses.ascii import isalpha, isdigit
import sys

def encode(shift: int):
    result = ''
    for i in sys.argv[2]:
        if i.isalpha():
            result += chr((ord(i) + shift) % 26 +)
        else:
            result += i
    return result

def decode(shift: int):
    pass

if __name__ == '__main__':
    if len(sys.argv) == 4:
        if sys.argv[3].isdigit():
            shift = int(sys.argv[3])
        else:
            raise Exception('shift not a num')
        if sys.argv[1] == 'encode':
            print(encode(shift))
        elif sys.argv[1] == 'decode':
            print(decode(shift))
        else:
            raise Exception('fuck')




