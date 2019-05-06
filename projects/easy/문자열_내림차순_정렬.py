def desc_sort_string(s):
    # a = list(s)
    # lower = []
    # bigger = []
    # for x in a:
    #     if x.islower():
    #         lower.append(x)
    #     else :
    #         bigger.append(x)
    #
    # lower.sort(reverse=True)
    # bigger.sort(reverse=True)
    # return ''.join(lower)+''.join(bigger)

    # sort(reverse=True) automatically sorts string in to reverse order
    # lower case first then bigger
    return ''.join(sorted(list(s), reverse=True))



def main():
    a = input("Input a string \n")
    print('answer = {}'.format(desc_sort_string(a)))

if __name__ == '__main__':
    main()



