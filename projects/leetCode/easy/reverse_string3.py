class Solution:
    def reverse_string(self, x):
        li = x.split(' ')
        result = ''
        for i in li:
            item = list(i)
            item.reverse()
            result += ''.join(item) + ' '
        return result.rstrip()


def main():
    a = Solution()
    print(a.reverse_string("Let's take LeetCode contest"))


if __name__ == '__main__':
    main()
