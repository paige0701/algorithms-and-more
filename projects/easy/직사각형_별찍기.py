def print_square(a,b):

    for i in range(int(b)):
        for j in range(int(a)):
            print("*", end = '')
        print('')

    print('=----------------------------------=')
    # 이렇게 똑똑한 방법이 ?

    print(('*' * int(a) + '\n') * int(b))


def main():
    a = input('input two numbers with space in between\n')
    b = a.split(" ")
    print_square(b[0],b[1])

if __name__ == '__main__':
    main()
