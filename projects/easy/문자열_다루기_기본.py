def is_numeric(s):
    if 1 < len(s) < 8:
        if len(s) == 4 or len(s) == 6:
            return s.isnumeric()

def main():
    a = input("Input a string \n")
    print('answer = {}'.format(is_numeric(a)))

if __name__ == '__main__':
    main()

