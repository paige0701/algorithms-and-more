"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution:
    def removeDuplicates(self, nums):

        result = []
        for i in nums:
            if i not in result:
                result.append(i)
        return result

if __name__ == '__main__':
    a = Solution()
    print(a.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))