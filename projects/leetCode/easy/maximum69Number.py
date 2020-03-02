"""
Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

"""


class Solution:
    def maximum69Number(self, num: int) -> int:

        return int(str(num).replace('6', '9', 1))
if __name__ == '__main__':
    s = Solution()
    print(s.maximum69Number(9669))


