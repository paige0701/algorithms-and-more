def sum_of_divisors(s):
    result = 0
    for i in range(1, s+1):
        if s%i == 0:
            result+=i
    return result





def main():
    a = int(input("Input a string \n"))
    print('answer = {}'.format(sum_of_divisors(a)))

if __name__ == '__main__':
    main()
