class Solution:
    def reverse_only_letters(self, S):

        letters = [x for x in S if x.isalpha()]
        result = []
        for x in S:
            if x.isalpha():
                result.append(letters.pop())
            else:
                result.append(x)
        return ''.join(result)


if __name__ == '__main__':
    a = Solution()
    print(a.reverse_only_letters('ab-cd'))