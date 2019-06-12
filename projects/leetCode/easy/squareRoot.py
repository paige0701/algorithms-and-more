# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
from math import sqrt
class Solution:
    def square_root(self, x:int) -> int:
        return int(sqrt(x))

def main():
    a = Solution()
    print(a.square_root(4))


if __name__ == '__main__':
    main()
