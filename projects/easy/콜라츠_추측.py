def collatz_conjecture(num):

    no = 0
    result = num
    while result != 1:
        if result % 2 == 0:
            result = result//2
        else:
            result = (result * 3) + 1
        no += 1
        
        if result == 1:
            break

        if no == 500:
            no = -1
            break

    return no


def main():
    num = int(input('input a number : \n'))
    print(collatz_conjecture(num))


if __name__ == '__main__':
    main()
