"""
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

"""


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        """
        이건 O(n^2)인거같은데 ..
        """
        result = 0
        for i in grid:
            for index, j in enumerate(i):
                if i[index] < 0:
                    result += 1


        grid = [
        [ 4,  3,   2, -1],
        [ 3,  2,   1, -1],
        [ 1,  1,  -1, -2],
        [-1, -1,  -2, -3]
        ]
        """
        [
        [ 4,  3,   2, -1],
        [ 3,  2,   1, -1],
        [ 1,  1,  -1, -2],
        [-1, -1,  -2, -3]
        ]
        
        이것을 잘 보아야한다. 먼저 grid[0][3] 을 체크하고 그것이 0 보다 작다면 
        그 컬럼은 다 0보다 작다는 것이라는것은 인지해야한다.
        
        그 다음 row 로 내려간다. grid[2][2] 가 0 보다 작으면 그 아래 컬럼은 다 0 보다 작다는 뜻
        
        이걸 도대체 어떻게 생각해 내는거지 ~? 대단하네 ..ㅎ
        """

        m, n = len(grid), len(grid[0])
        r, c, result = 0, n-1, 0

        while r < m and c >=0:
            if grid[r][c] < 0:
                result += m-r
                c-=1
            else:
                r+=1

        return result