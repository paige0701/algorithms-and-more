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
    1, 1, 2, 3, 5, 8, 13


    """
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    print(factorial(5))
    print(is_palindrome('xyzzyxx'))
    print(fib(6))