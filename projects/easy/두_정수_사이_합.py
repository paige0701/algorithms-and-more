def add_numbers_in_between(num1, num2):

    if num1 == num2:
        return num1

    if num1 > num2:
        num1, num2 = num2, num1

    result = sum(range(num1, num2+1))
    # for x in range(num1, num2+1):
    #     result+=x
    return result



def main():
    a = int(input("first number:\n"))
    b = int(input("second number:\n"))
    print('answer = {}'.format(add_numbers_in_between(a,b)))

if __name__ == '__main__':
    main()

