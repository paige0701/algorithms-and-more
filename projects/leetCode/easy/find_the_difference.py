class Solution:
    def isAnagram(self, s,t):

        li = list(t)
        for i in s:
            li.remove(i)

        return ''.join(li)




if __name__ == '__main__':
    a = Solution()
    print(a.isAnagram("abcd", "abcde"))