class Solution:
    def decompressRLElist(self, nums):
        li = []
        for i in range(1, len(nums), 2):
            print(i)
            li += [nums[i]]*nums[i-1]
        return li


if __name__ == '__main__':
    solution = Solution()
    print(solution.decompressRLElist([1,2,3,4]))
