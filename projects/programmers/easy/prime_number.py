def sum_of_prime_numbers(val):
    result = 0
    for num in range(val + 1):
        # prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                result += num
    print(result)


def main():
    print(sum_of_prime_numbers(5))

if __name__ == '__main__':
    main()

