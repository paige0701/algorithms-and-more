"""

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = result = 0
        for i in s:
            if i == 'L':
                counter +=1
            else:
                counter -=1
            if counter == 0:
                result += 1
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.balancedStringSplit('LRRL'))