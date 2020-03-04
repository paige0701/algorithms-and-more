"""
Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
"""
class Solution:
    def flipAndInvertImage(self, A):
        # for i in A:
        #     i.reverse()
        #     print(i)
        #     for index,val in enumerate(i):
        #         if i[index] == 0 :
        #             i[index] = 1
        #         else:
        #             i[index] =0

        return [[i-1 for i in row[::-1]] for row in A]


if __name__ == '__main__':
    solution = Solution()
    print(solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))