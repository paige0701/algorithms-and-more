import collections


def main(nums):

    # if len(nums) == 0:
    #     return False
    # else:
    #     map1 = {}
    #
    #     count = 0
    #     result = False
    #     while count < len(nums):
    #         key = str(nums[count])
    #         if map1.get(key) is None:
    #             map1[key] = key
    #             count = count + 1
    #         else:
    #             result = True
    #             break
    #     return result

    # using collections
    # a = nums
    # b = collections.Counter(a).most_common()
    # return True if b[0][1] > 1 else False

    #using set
    # nums.sort()
    # aSet = list(set(nums))
    # aSet.sort()
    # return aSet != nums

    # fastest
    return len(nums) != len(set(nums))


if __name__ == '__main__':
    print(main([1,2,3,4,1]))