"""
Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

"""


class Solution:
    def bitwise_complement(self, N):
        binary = "{0:b}".format(N)
        complement = ''.join(['1' if x == '0' else '0' for x in binary])
        return int(complement, 2)


if __name__ == '__main__':
    a = Solution()
    print(a.bitwise_complement(11))