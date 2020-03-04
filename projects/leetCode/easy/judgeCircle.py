"""

Input: "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
"""


class Solution:
    def judgeCircle(self, moves):
        result = [0,0]
        for i in moves:
            if i == 'U':
                result[0] += 1
            elif i == 'D':
                result[0] -= 1
            elif i == 'L':
                result[1] += 1
            else:
                result[1] -= 1
        print(result)
        print(moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D'))
        return result[0] == 0 and result[1] == 0

if __name__ == '__main__':
    solution = Solution()
    print(solution.judgeCircle("LDRRLRUULR"))
