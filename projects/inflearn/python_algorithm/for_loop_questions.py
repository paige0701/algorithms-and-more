def find_odd_numbers():

    num = int(input("Insert a number"))
    result = filter(lambda x: x % 2 == 1, [i for i in range(1, num+1)])
    return list(result)


def get_sum():
    num = int(input('Insert a number'))
    result = 0
    for i in range(1, num+1):
        result += i

    # return (num * (num+1))//2 another way of finding sum O(1)

    return result  # O(n)


def find_all_divisor():
    num = int(input('Insert a number'))
    return list(filter(lambda x: x% 2 == 0, [i for i in range(1, num+1)]))


if __name__ == '__main__':
    # print(find_odd_numbers())
    # print(get_sum())
    print(find_all_divisor())