"""

Given two arrays, write a function to compute their intersection.


"""

class Solution:
    def intersection(self, nums1, nums2):
        one = set(nums1)
        two = set(nums2)

        return list(one & two)


if __name__ == '__main__':
    a = Solution()
    a.intersection([1,2,2,1], [2,2])