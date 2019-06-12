def test(a,b):
    print([a*i for i in range(1, b+1)])


def main():
    a = int(input('input a: \n'))
    b = int(input('input b: \n'))

    test(a,b)

if __name__ == '__main__':
    main()
