def get_middle_string(val):

    length = len(val)

    if length > 100 or length < 1:
        return

    if length % 2 == 1:
        return val[length//2]
    else:
        return val[length//2-1:length//2+1]


def main():
    print(get_middle_string(''))

if __name__ == '__main__':
    main()

