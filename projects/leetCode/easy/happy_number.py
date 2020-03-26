class Solution:
    def is_happy(self, number):

        seen = set()
        while number not in seen:
            seen.add(number)
            number = sum([int(i)**2 for i in str(number)])
        return number == 1


if __name__ == '__main__':
    a = Solution()
    print(a.is_happy(7))