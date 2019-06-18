def factorial(number):

    if number == 1:
        return 1
    elif number > 1:
        return number * factorial(number-1)

"""
    output = 1
    for i in range(1, number+1):
        output *= i
    return output
"""

if __name__ == '__main__':

    print(factorial(3))
