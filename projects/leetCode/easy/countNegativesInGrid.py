"""
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

"""


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        for i in grid:
            for index, j in enumerate(i):
                if i[index] < 0:
                    result += 1

        return result