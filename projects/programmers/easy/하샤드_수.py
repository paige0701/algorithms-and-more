def harshad(num):

    result = sum(int(x) for x in list(str(num)))
    print(result)
    return num % result == 0

def main():
    num = int(input('input a number : \n'))
    print(harshad(num))

if __name__ == '__main__':
    main()
