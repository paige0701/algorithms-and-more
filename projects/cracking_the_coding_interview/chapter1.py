import collections

def one_is_unique(string):
    print(len(string) == len(set(string)))

def two_check_permutation(str1, str2):
    print(sorted(str1) == sorted(str2))

def three_urlify(str1):
    str1 = str1.rstrip()
    print(str1.replace(' ', '%20'))

def four_palindrome_permutations(str1):
    str1 = str1.replace(' ', '')
    num = 0
    for i in collections.Counter(str1).values():
        print(i)
        if i % 2 != 0:
            num +=1

    return not num > 1


if __name__ == '__main__':
    # one_is_unique('abcc')
    # two_check_permutation('abc','ccc')
    # three_urlify('Mr John Smith     ')
    print(four_palindrome_permutations('tact coa'))