def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def is_palindrome(string):

    # base case 1 - if string length is 0 or 1, it is palindrome
    if len(string) <= 1:
        return True

    # if first and last letter is different, it is NOT a palindrome
    if first_character(string) != last_character(string):
        return False

    # recursive
    return is_palindrome(string[1:-1])

def first_character(string):
    return string[0]


def last_character(string):
    return string[-1]


def fib(n):
    """
    fibonacci starts from two ones
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,

    1 + 1 = 2
    1 + 2 = 3
    2 + 3 = 5
    3 + 5 = 8
    ...
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def num_of_ways(n):
    """

    개구리는 1 or 2 개의 step 만 점프 할 수 있다.
    끝까지 가는데 몇가지 방법이 있냐?

    🐸 ㅡ.ㅡ.ㅡ.ㅡ.ㅡ.ㅡ.ㅡ.ㅡ.ㅡ.ㅡ.ㅡ

    피보나치랑 같다 !
    """

    if n == 0 or n==1:
        return 1
    return num_of_ways(n-1) + num_of_ways(n-2)



if __name__ == '__main__':
    print(factorial(5))
    print(is_palindrome('xyzzyxx'))
    print(fib(5))
    print(fib(10))
    print(num_of_ways(11))