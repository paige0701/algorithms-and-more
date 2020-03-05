"""
Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
"""

class Solution:
    def island_parameter(self, arr):
        result = 0
        for i, iv in enumerate(arr):
            for j, jv in enumerate(arr[i]):

                # if it is an island
                if arr[i][j] == 1:
                    if i == 0 or arr[i-1][j] == 0:
                        result += 1
                    if j == 0 or arr[i][j-1] == 0:
                        result +=1
                    if j == len(arr[i])-1 or arr[i][j+1] == 0:
                        result +=1
                    if i == len(arr)-1 or arr[i+1][j] == 0:
                        result +=1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.island_parameter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))