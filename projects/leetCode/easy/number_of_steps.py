
class Solution:
    def numberOfSteps (self, result: int) -> int:

        times = 0
        while result > 0:
            if result % 2 == 0:
                result//=2
            else:
                result-=1
            times+=1
        return times


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfSteps(14))