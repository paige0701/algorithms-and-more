def return_true_if_number_equal(val):

    if len(val) > 50:
        return

    upper_case = val.upper()

    number_of_y = upper_case.count('Y')
    number_of_p = upper_case.count('P')

    # if number_of_p == 0 and number_of_y == 0:
    #     return True
    #
    # if number_of_p == number_of_y:
    #     return True
    #
    # return True if number_of_p > number_of_p else False

    ## this is better
    return number_of_y == number_of_p


def main():
    a = input("Input a string \n")
    print('answer = {}'.format(return_true_if_number_equal(a)))

if __name__ == '__main__':
    main()

