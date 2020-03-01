class Solution:
    def smaller_numbers_than_current(self, nums):

        # RESULT 1
        sortedA = sorted(nums)
        result1 = [sortedA.index(i) for i in nums]

        # RESULT2
        indices = {}
        for i, v in enumerate(sorted(nums)):
            indices.setdefault(v,i)   # insert if key does not exist!!
        result2 = [indices[i] for i in nums]

        return result2


if __name__ == '__main__':
    solution = Solution()
    print(solution.smaller_numbers_than_current([8,1,2,2,3]))

