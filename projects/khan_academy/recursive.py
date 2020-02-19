def factorial(n):

    """
            return      state

    F(5)    5 * F(4)    Pause
    F(4)    4 * F(3)    Pause
    F(3)    3 * F(2)    Pause
    F(2)    2 * F(1)    Pause
    F(1)    1 * F(0)    Pause
    F(0)    1
    F(1)    1 * 1       Resume
    F(2)    2 * 1       Resume
    F(3)    3 * 2       Resume
    F(4)    4 * 6       Resume
    F(5)    5 * 24      Resume

    = 120

    """


    print('iam calculating ', n , '\n')
    if n == 0:
        return 1
    f = n * factorial(n-1)
    print('F(',n,') is ', f)
    return f

def is_palindrome(string):

    """
    TO check if a string is a palindrome, reversed string must be same
    reverse a 'appa' it's same so 'appa; is a palindrome


    a = 'appa'
    a[::-1] to reverse a list
    """

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


def fib_with_memoization(n):
    a = [None] * (n+1)
    return fib2(n, a)

def fib2(n, memo):

    if memo[n] is not None:
        return memo[n]  # None 이 아니면 이미 값이 있다는 것이기 때문에 그 값을 그냥 쓰면 된다.
    if n == 0 or n == 1:
        result = 1
    else:
        result = fib2(n-1, memo) + fib2(n-2, memo)
    memo[n] = result


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
    # print(is_palindrome('xyzzyxx'))
    # print(fib(5))
    # print(fib(10))
    # print(num_of_ways(11))
    # print(fib_with_memoization(2))