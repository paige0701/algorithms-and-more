"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

"""

class Solution:
    def twoSum(self, numbers, target):
        dic = {}
        # for i,v in enumerate(numbers):
        #     if (target-v in numbers) and (target-v != i):
        #         id = numbers.index(target-v)
        #         result.append(i+1)
        #         result.append(id+1)
        #         return result

        for index,value in enumerate(numbers):
            if target-value in dic:
                return [dic[target-value]+1, index+1]
            dic[value] = index





def main():
    a = Solution()
    print(a.twoSum([-1,0],-1))


if __name__ == '__main__':
    main()

