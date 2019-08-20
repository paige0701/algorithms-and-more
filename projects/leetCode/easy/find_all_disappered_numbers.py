class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_set = set(nums)

        diff = set([i for i in range(1, len(nums)+1)])

        return list(diff.difference(num_set))


if __name__ == '__main__' :
    solution = Solution()
    print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

