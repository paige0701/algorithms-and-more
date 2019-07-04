import collections

class Solution:
    def isAnagram(self, s,t):

        return collections.Counter(s) == collections.Counter(t)


if __name__ == '__main__':
    a = Solution()
    print(a.isAnagram("rat", "tar"))