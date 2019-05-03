def add_numbers_in_between(num1, num2):

    if num1 == num2:
        return num1

    if num1 > num2:
        num1, num2 = num2, num1

    result = 0

    for x in range(num1, num2+1):
        result+=x
    return result

def main():
    print(add_numbers_in_between(5,1))
    # 1 + 2 + 3 = 6

if __name__ == '__main__':
    main()

