class Solution:
    def add_digits(self, num):

        if len(str(num)) == 1:
            return num
        else:
            integers = [int(i) for i in str(num)]
            total = sum(integers)
            return self.add_digits(total)


if __name__ == '__main__':
    a = Solution()
    print(a.add_digits(38))