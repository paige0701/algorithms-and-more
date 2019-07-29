# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
from collections import Counter, OrderedDict


def find_single_number(nums):



    # using bit manipulation

    """

    0 ^ 1 = 1
    1 ^ 1 = 0

    that is why ^= returns a unique number.
    so clever!

    """

    # a = 0
    # for i in nums:
    #     a^=i
    # return a

    duplicated_list = []
    for i in nums:
        if i not in duplicated_list:
            duplicated_list.append(i)
        else:
            duplicated_list.remove(i)
    return duplicated_list.pop()




if __name__ == '__main__':
    print(find_single_number([4,1,2,2,1]))